"""
Assignment 5 - Building a Robust ETL Pipeline with PostgreSQL & psycopg2
Pure business-logic module (no SQL, no database objects).

Student: Nawaraj Tamang

These functions take and return plain Python data structures only, so they
can be unit tested (see test_transform.py) without a live database
connection. All database-facing code lives in the notebook.
"""

from collections import defaultdict

# Thresholds from the original class14 pipeline. Boundaries are inclusive
# on the lower edge of each tier (>= not >), so "exactly 5000" is already
# Standard and "exactly 20000" is already Premium.
PREMIUM_THRESHOLD = 20000
STANDARD_THRESHOLD = 5000

# A single transaction at/above this amount marks a customer high-value,
# independent of their running total.
HIGH_VALUE_TXN_THRESHOLD = 10000


def transform(transaction_rows):
    """Aggregate raw transaction rows into a per-customer total.

    Parameters
    ----------
    transaction_rows : list[dict]
        Each dict has at least 'customer_id' and 'amount'.

    Returns
    -------
    dict[int, float]
        customer_id -> total_transactions (sum of amount)
    """
    totals = defaultdict(float)
    for row in transaction_rows:
        totals[row["customer_id"]] += float(row["amount"])
    return dict(totals)


def high_value_flag(transaction_rows_for_customer):
    """True if any single transaction for this customer is >= the
    high-value threshold. Pure function: takes a list of that one
    customer's transaction dicts, returns a bool.
    """
    return any(
        float(t["amount"]) >= HIGH_VALUE_TXN_THRESHOLD
        for t in transaction_rows_for_customer
    )


def categorize(total_transactions, has_defaulted_loan=False):
    """Categorize a customer.

    A customer with any defaulted loan is always "At Risk", regardless of
    transaction total. Otherwise, fall back to the original transaction-total
    thresholds from the class14 pipeline.
    """
    if has_defaulted_loan:
        return "At Risk"
    if total_transactions >= PREMIUM_THRESHOLD:
        return "Premium"
    if total_transactions >= STANDARD_THRESHOLD:
        return "Standard"
    return "Basic"


def transform_loans(loan_rows):
    """Aggregate raw loan rows into per-customer exposure figures.

    Parameters
    ----------
    loan_rows : list[dict]
        Each dict has at least 'customer_id', 'principal', and 'status'.
        status is one of 'active', 'paid_off', 'defaulted'.

    Returns
    -------
    dict[int, dict]
        customer_id -> {
            "total_loan_exposure": float,   # sum of principal, active loans only
            "active_loan_count": int,       # count of active loans
            "has_defaulted_loan": bool,     # True if any loan is defaulted
        }
    """
    summary = defaultdict(lambda: {
        "total_loan_exposure": 0.0,
        "active_loan_count": 0,
        "has_defaulted_loan": False,
    })

    for loan in loan_rows:
        cid = loan["customer_id"]
        entry = summary[cid]
        if loan["status"] == "active":
            entry["total_loan_exposure"] += float(loan["principal"])
            entry["active_loan_count"] += 1
        elif loan["status"] == "defaulted":
            entry["has_defaulted_loan"] = True

    return dict(summary)


def build_account_summary(customer_ids, transaction_rows, loan_rows):
    """Combine transform() and transform_loans() into one row per customer,
    ready to hand to load_summary(). Still pure - no SQL, no db object.

    Every customer_id passed in appears exactly once in the result, even
    with zero transactions or zero loans.
    """
    totals = transform(transaction_rows)
    loan_summary = transform_loans(loan_rows)

    txns_by_customer = defaultdict(list)
    for row in transaction_rows:
        txns_by_customer[row["customer_id"]].append(row)

    rows = []
    for cid in customer_ids:
        total = totals.get(cid, 0.0)
        loans = loan_summary.get(cid, {
            "total_loan_exposure": 0.0,
            "active_loan_count": 0,
            "has_defaulted_loan": False,
        })
        rows.append({
            "customer_id": cid,
            "total_transactions": total,
            "total_loan_exposure": loans["total_loan_exposure"],
            "active_loan_count": loans["active_loan_count"],
            "high_value_flag": high_value_flag(txns_by_customer.get(cid, [])),
            "category": categorize(total, has_defaulted_loan=loans["has_defaulted_loan"]),
        })
    return rows
