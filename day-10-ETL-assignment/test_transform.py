"""
Assignment 5 - Building a Robust ETL Pipeline with PostgreSQL & psycopg2
Unit tests for the pure transformation functions in transform_logic.py.

Student: Nawaraj Tamang

Run with:  pytest test_transform.py -v
None of these tests touch a database - they only exercise plain Python
functions with plain Python data structures, per the assignment's Task 3
requirement.
"""

from transform_logic import (
    categorize,
    transform,
    transform_loans,
    high_value_flag,
    build_account_summary,
)


# ---------------------------------------------------------------------------
# categorize() - category boundaries and the "At Risk" override
# ---------------------------------------------------------------------------

def test_categorize_boundary_exactly_5000_is_standard():
    assert categorize(5000) == "Standard"


def test_categorize_boundary_exactly_20000_is_premium():
    assert categorize(20000) == "Premium"


def test_categorize_below_5000_is_basic():
    assert categorize(4999.99) == "Basic"


def test_categorize_defaulted_loan_overrides_high_transaction_total():
    # High transaction total would normally be "Premium", but a defaulted
    # loan must force "At Risk" regardless.
    assert categorize(50000, has_defaulted_loan=True) == "At Risk"


# ---------------------------------------------------------------------------
# transform_loans() - loan exposure aggregation
# ---------------------------------------------------------------------------

def test_transform_loans_customer_with_zero_loans_does_not_error():
    result = transform_loans([])
    assert result == {}


def test_transform_loans_active_only_counted_in_exposure():
    loans = [
        {"customer_id": 1, "principal": 10000, "status": "active"},
        {"customer_id": 1, "principal": 5000, "status": "paid_off"},
        {"customer_id": 1, "principal": 7000, "status": "active"},
    ]
    result = transform_loans(loans)
    assert result[1]["total_loan_exposure"] == 17000
    assert result[1]["active_loan_count"] == 2
    assert result[1]["has_defaulted_loan"] is False


def test_transform_loans_flags_defaulted_status():
    loans = [{"customer_id": 2, "principal": 3000, "status": "defaulted"}]
    result = transform_loans(loans)
    assert result[2]["has_defaulted_loan"] is True
    # A defaulted loan is not "active", so it contributes 0 to exposure.
    assert result[2]["total_loan_exposure"] == 0


# ---------------------------------------------------------------------------
# high_value_flag() - single-transaction threshold, unaffected by later changes
# ---------------------------------------------------------------------------

def test_high_value_flag_true_when_single_txn_over_threshold():
    txns = [{"amount": 250}, {"amount": 15000}]
    assert high_value_flag(txns) is True


def test_high_value_flag_false_when_all_txns_small():
    txns = [{"amount": 250}, {"amount": 999}]
    assert high_value_flag(txns) is False


# ---------------------------------------------------------------------------
# build_account_summary() - end-to-end pure aggregation, zero-loan customer
# ---------------------------------------------------------------------------

def test_build_account_summary_customer_with_zero_loans_and_zero_txns():
    rows = build_account_summary(
        customer_ids=[1, 2, 3],
        transaction_rows=[{"customer_id": 1, "amount": 100}],
        loan_rows=[{"customer_id": 2, "principal": 1000, "status": "active"}],
    )
    by_id = {r["customer_id"]: r for r in rows}

    # Customer 3 has no transactions and no loans at all.
    assert by_id[3]["total_transactions"] == 0
    assert by_id[3]["total_loan_exposure"] == 0
    assert by_id[3]["active_loan_count"] == 0
    assert by_id[3]["category"] == "Basic"
    # Every customer passed in appears exactly once.
    assert len(rows) == 3


def test_transform_sums_multiple_transactions_per_customer():
    rows = [
        {"customer_id": 1, "amount": 100},
        {"customer_id": 1, "amount": 250},
        {"customer_id": 2, "amount": 999},
    ]
    totals = transform(rows)
    assert totals[1] == 350
    assert totals[2] == 999
