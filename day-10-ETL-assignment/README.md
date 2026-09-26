Assignment 5 - Building a Robust ETL Pipeline with PostgreSQL and psycopg2

Nawaraj Tamang

Topics Covered

This assignment extends the class14 banking ETL pipeline with a new 'loans' table, a hardened database connection with retry and reconnect logic, an updated transformation and categorization rule that accounts for loan risk, an upsert-based load step, a full reconciliation report, and a suite of unit tests for the pure transformation logic. It runs against the real three-table banking dataset (201 customers, 279 accounts, 4,613 transactions) rather than a handful of made-up rows, the same data used in the Day 9 SQL practice notebook.

Exercises

Task 1 extends the schema with a 'loans' table ('loan_id', 'customer_id' as a foreign key to 'customers', 'principal', 'interest_rate', a 'status' column constrained to 'active', 'paid_off', or 'defaulted', and 'start_date'), plus two new columns on 'account_summary': 'total_loan_exposure' and 'active_loan_count'. All DDL uses 'CREATE TABLE IF NOT EXISTS', matching the idempotent style from the original 'create_schema'. Loans are seeded across three real customers ('customer_id' 1, 2, and 3 - Krishna Rai, Anita Lama, and Gita Pandey) with six rows spanning all three statuses. The dataset's one intentionally orphaned account row has been removed for now, so 'accounts.customer_id' is a plain inline foreign key; if that row needs to come back later for data quality testing, adding the constraint as NOT VALID and validating it afterward, the same pattern used in Day 9, is the way to reintroduce it without blocking the load.

Task 2 hardens 'DBConnection' with a 'reconnect' method and introduces a 'with_retry' decorator that wraps any database-facing function. On a 'psycopg2.OperationalError' it logs the attempt, rolls back the transaction (or reconnects if the connection itself has died), and retries up to three times before giving up. To prove this actually works rather than just looking plausible, the notebook opens a second admin connection and calls 'pg_terminate_backend' on the pipeline's own backend process mid-run, which produces a genuine 'OperationalError'. The very next call to a decorated extract function fails once, reconnects, and succeeds on retry, and the full sequence is visible in 'etl.log'.

Task 3 keeps all business logic in 'transform_logic.py' as plain functions with no SQL and no database object, so they can be tested without a live connection. 'transform' sums transaction amounts per customer, 'high_value_flag' checks whether any single transaction clears a threshold, 'transform_loans' aggregates loan exposure and active loan counts per customer, and 'categorize' now takes a loan-risk flag: any customer with a defaulted loan is always categorized 'At Risk', regardless of transaction total.

Task 4 updates the upsert in 'load_summary' to write the two new loan columns alongside the original fields, and extends 'verify' into a fuller reconciliation report that joins 'customers' to 'account_summary' and confirms every customer appears exactly once.

Task 5 adds eleven pytest tests in 'test_transform.py' covering the category boundaries at exactly 5000 and exactly 20000, the defaulted-loan override, a customer with zero loans, and the high-value-flag logic, all passing against 'transform_logic.py' alone.

How to Run

Install dependencies with 'pip install -r requirements.txt'. Copy '.env.example' to '.env' and fill in real PostgreSQL credentials; this file is never committed. Open 'Assignment_NawarajTamang.ipynb' in VS Code with the Jupyter extension and run all cells top to bottom after a kernel restart - it connects to PostgreSQL, creates and verifies the schema, reloads the real CSV data from the 'data' folder, runs the full extract-transform-load pipeline, prints a reconciliation report, and then deliberately terminates its own database connection mid-pipeline to demonstrate the retry logic, with the details written to 'etl.log'. To run the unit tests on their own, use 'pytest test_transform.py -v'; they only import 'transform_logic.py' and never touch a database.

What I Learned

Splitting the pure business logic into its own module made Task 5 far easier than expected. Because 'categorize', 'transform_loans', and 'high_value_flag' only take and return plain dicts and lists, all eleven pytest tests run in milliseconds with no database setup, and the notebook just imports the same functions the tests exercise. Building the retry decorator also taught me the difference between a broken transaction and a broken connection - my first version only called 'db.rollback()' on failure, which works when the transaction is aborted but the connection is still alive, but when I actually killed the connection to test it, 'rollback()' itself raised, since there was no connection left to roll back. Adding a 'reconnect' method to 'DBConnection' and falling back to it when rollback fails made the recovery genuine rather than cosmetic.

Challenges Faced

The biggest challenge was proving the retry logic actually worked rather than just looking correct on paper. Closing the connection with 'db.conn.close()' only produced a 'psycopg2.InterfaceError', not the 'OperationalError' the assignment calls out, so a naive test would have silently done nothing. Opening a second admin connection and calling 'pg_terminate_backend' on the pipeline connection's backend process id produces a genuine 'OperationalError' on the next query, which is what actually shows up as a real, logged retry-then-recover cycle in 'etl.log'.

The second challenge was the categorization boundary logic in Task 3: the assignment's example boundaries only make sense if the thresholds are inclusive on the lower edge, otherwise a customer at exactly 5000 would fall into the wrong tier. Writing the boundary tests first made this explicit before writing a single line of the real 'categorize' function. Against the real dataset, where the average transaction is around NPR 30,000 and most customers have twenty or more transactions, nearly every customer's running total clears the Premium threshold, so the category distribution skews heavily toward Premium. The thresholds are kept exactly as specified rather than recalibrated, since the boundary test cases are pinned to those values, but it is worth knowing going in that the output looks unbalanced for that reason and not because of a bug.

The third challenge was a silent 'COPY' failure the first time real CSV data replaced the toy sample rows. The files use Windows-style CRLF line endings, and re-running the notebook after the tables already existed meant 'CREATE TABLE IF NOT EXISTS' skipped rebuilding them with the new columns, so 'COPY' was quietly trying to load sixteen-column rows into an old three-column table. Dropping the stale tables before recreating the schema, and stripping the CRLFs from the CSVs first, fixed both issues.
