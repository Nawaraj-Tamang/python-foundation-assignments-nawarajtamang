# Day 09 -- Python for Data Engineering: Banking SQL Practice

## Topics Covered

- Connecting to PostgreSQL securely with `python-dotenv`, loading credentials from a git-ignored `.env` file instead of hardcoding them, with an explicit check that raises a clear error if any variable is missing
- Logging every operation -- connect, schema creation, each query and its row count, close -- to `log.log` via Python's `logging` module, instead of relying on `print()` output that scrolls away
- Wrapping the connection in a small `DBConnection` OOP class (`cursor()`, `commit()`, `rollback()`, `close()`) so every part of the notebook shares one connection
- Creating three related tables (`customers`, `accounts`, `transactions`) with explicit `CREATE TABLE` DDL, matching PostgreSQL types to each column
- Bulk-loading CSVs into PostgreSQL with `COPY ... WITH (FORMAT csv, HEADER true, NULL '')`, which is dramatically faster than row-by-row `INSERT` and converts blank CSV fields into real SQL `NULL`s
- Adding a foreign key as `NOT VALID` after data load, rather than inline in `CREATE TABLE`, to tolerate an intentionally orphaned row without blocking the load
- Writing and running 40 SQL queries covering joins, aggregation, subqueries (scalar, correlated, `EXISTS`/`NOT EXISTS`, `IN`, inline views), set operations (`UNION`, `UNION ALL`, `INTERSECT`, `EXCEPT`), CTEs (single and chained), views and materialized views, window functions (`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`, running totals, `NTILE`), data-quality checks, `CASE` bucketing, and a transactional `UPDATE` + `INSERT` block
- Running an `UPDATE` and multiple related `INSERT`s as one all-or-nothing transaction, committing only on full success and rolling back on any failure

## Exercises

The assignment is delivered as a single notebook, `banking_sql_practice.ipynb`, working against a small banking dataset (`customers`, `accounts`, `transactions` -- 201 customers, 280 accounts, 4,613 transactions): customer demographics, account details, and transaction history.

The 40 questions are grouped by topic:

1. **Joins (Q1--Q5)** -- inner join active accounts to their owner, find customers with no account and accounts with no customer (`LEFT JOIN`), label every match with `FULL OUTER JOIN` + `CASE`, and join across all three tables at once.
2. **Aggregation (Q6--Q10)** -- total balance per branch, top 5 branches, account types with `HAVING AVG(balance) > 50000`, customers with multiple accounts, and the highest-volume branch/account-type combo.
3. **Subqueries (Q11--Q16)** -- customers above the overall average balance, accounts above their own account-type's average (correlated subquery), `EXISTS`/`NOT EXISTS`, `IN`, and an inline view (subquery in `FROM`).
4. **Set Operations (Q17--Q20)** -- `UNION`, `UNION ALL`, `INTERSECT`, and `EXCEPT` across Savings/Checking/Fixed Deposit account holders.
5. **CTEs & Views (Q21--Q25)** -- single and chained `WITH` clauses, a `CREATE VIEW` for active accounts, and a `CREATE MATERIALIZED VIEW` refreshed with `CONCURRENTLY`.
6. **Window Functions (Q26--Q31)** -- most recent transaction per account (`ROW_NUMBER`), balance ranking (`RANK`/`DENSE_RANK`), previous/next transaction (`LAG`/`LEAD`), and a running total.
7. **Data Quality (Q32--Q33)** -- duplicate customers and orphaned accounts, both deliberately seeded into the dataset to give these queries something real to find.
8. **CASE & Transactions (Q34--Q35)** -- bucketing account balances into Low/Medium/High, then a full transaction block that deducts a maintenance fee and logs a matching transaction row, safely rolled back on failure.
9. **Compliance & Misc (Q36--Q40)** -- income quartiles (`NTILE`), low-credit-score/high-balance customers, flagged transactions, expired-KYC customers with active accounts, and joint accounts above their branch average (another correlated subquery).

Each question runs through a shared `run()` helper that executes the query, logs the row count, and prints a short preview (up to 5 rows) so full output stays readable, while the complete result set is still returned for further use.

## How to Run

This day uses a Jupyter notebook against a live PostgreSQL database, so there's a setup step beyond just installing packages:

```bash
cd day-09-banking-sql-practice
pip install -r requirements.txt
cp .env.example .env   # then fill in your real DB credentials
```

Open `banking_sql_practice.ipynb` in VS Code (Jupyter extension) or JupyterLab and run all cells top to bottom. The notebook connects to PostgreSQL with credentials from `.env` (never committed -- see `.gitignore`), creates the three tables, loads `data/*.csv` into them, adds the orphan-tolerant foreign key, then runs all 40 queries. The last cell closes the connection cleanly.

## What I Learned

The biggest shift from Day 08 was working with three related tables instead of one flat file -- almost every query needed at least one join, and the difference between `LEFT JOIN ... WHERE x IS NULL` (find what's missing) and `INNER JOIN` (find what matches) became a lot more concrete once there were real orphaned rows to catch with it. Window functions were the other big unlock: once `PARTITION BY` clicked as "restart the calculation for each group," `ROW_NUMBER`, `RANK`, `LAG`, and a running-total `SUM() OVER (... ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)` all turned out to be the same underlying idea applied slightly differently, rather than four things to memorize separately.

Building the transaction block for Q35 also made "commit vs. rollback" feel real for the first time -- snapshotting the affected accounts *before* running the `UPDATE` (since `balance - 500` is only meaningful pre-update), then doing the `UPDATE` and every related `INSERT` inside one `try`/`except`, committing only if everything succeeds. It's the same pattern as Day 08's `.env` validation -- fail loudly and completely rather than leaving things half-done.

## Challenges Faced

The first surprise had nothing to do with SQL: the "CSV" files I was given for `customers`, `accounts`, and `transactions` were actually `.xlsx` files saved with a `.csv` extension -- they wouldn't parse as text at all. Renaming a copy to `.xlsx` and opening it with `openpyxl` confirmed it, and from there it was a matter of exporting proper, clean CSVs before `COPY` would touch them.

The second was the orphaned-row problem in Q3/Q33: one `accounts` row references a `customer_id` that doesn't exist in `customers`, which is intentional (it's what the Data Quality questions are supposed to catch) -- but it meant a normal inline `FOREIGN KEY` in `CREATE TABLE` would reject the load outright, since Postgres validates every existing row by default. Adding the constraint separately with `NOT VALID` after the data was already loaded solved it -- new rows are still checked going forward, but the one seeded bad row doesn't block the schema from being built.

The third was in Q25: `REFRESH MATERIALIZED VIEW CONCURRENTLY` silently refused to run until I added a `UNIQUE INDEX` on the materialized view first -- Postgres needs that unique index to figure out which rows changed without locking readers out during the refresh, which isn't obvious from the error message alone until you look it up.
