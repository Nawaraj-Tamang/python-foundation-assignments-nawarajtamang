# Day 8 -- Python for Data Engineering: SQL Operators Assignment

## Topics Covered

- Loading a real dataset with `pd.read_csv()` and cleaning float-with-blanks columns (`phone`, `emergency_contact`) back into clean nullable strings
- Connecting to PostgreSQL securely with `python-dotenv`, loading credentials from a git-ignored `.env` file instead of hardcoding them
- Creating a table with an explicit `CREATE TABLE` statement, matching PostgreSQL types (`NUMERIC`, `DATE`, `VARCHAR`) to each of the dataset's 29 columns
- Loading a DataFrame into PostgreSQL with `df.to_sql()` via a SQLAlchemy engine, then verifying the row count with a sanity-check query
- Writing and running 50 SQL queries from Python with `pd.read_sql_query()`, covering arithmetic, comparison, logical, `LIKE`, `IN`, `BETWEEN`, and `IS NULL` / `IS NOT NULL` operators
- Combining multiple operator types in a single query to answer more realistic, multi-condition business questions

## Exercises

The assignment is delivered as a single notebook, `employee_Assignment.ipynb`, working against Cedar Grove -- er, against the company's employee records in `Employees.csv` (150 employees, 29 columns): employee details, department, salary, performance, and contact info.

The 50 questions are grouped by SQL operator:

1. **Arithmetic Operators (Q1--Q6)** -- calculate increased/reduced salary, annual salary, average monthly bonus, a remainder with `%`, and total compensation.
2. **Comparison Operators (Q7--Q12)** -- filter employees by salary, age, performance rating, experience, department, and employment status using `>`, `<`, `>=`, `<=`, `=`, and `<>`.
3. **Logical Operators (Q13--Q18)** -- combine conditions with `AND`, `OR`, and `NOT` to narrow down employees by city, department, remote status, and salary together.
4. **LIKE Operator (Q19--Q24)** -- pattern-match names, job titles, and email domains with `%` wildcards.
5. **IN Operator (Q25--Q28)** -- match employees against a set of cities, departments, employment types, or education levels in one condition.
6. **BETWEEN Operator (Q29--Q33)** -- filter by ranges of age, salary, performance rating, experience, and join date.
7. **IS NULL / IS NOT NULL (Q34--Q38)** -- find employees with missing (or present) email, phone, emergency contact, and certification data.
8. **Mixed Challenge (Q39--Q50)** -- combine several operator types per query, closing with two queries that also compute derived columns (`annual_salary`, `total_compensation`) alongside the filtering.

Each question has its own markdown cell with the prompt, followed by a code cell building the query string, running it through a shared `run_query()` helper, and displaying up to 20 result rows.

## How to Run

This day uses a Jupyter notebook against a live PostgreSQL database, so there's a setup step beyond just installing packages:

```bash
cd day-08-SQL-assignments
pip install psycopg2-binary sqlalchemy pandas python-dotenv
cp .env.example .env   # then fill in your real DB credentials
```

Open `employee_Assignment.ipynb` in VS Code (Jupyter extension) or JupyterLab and run all cells top to bottom. The notebook connects to PostgreSQL with credentials from `.env` (never committed -- see `.gitignore`), creates the `employees` table, loads `Employees.csv` into it, then runs all 50 queries. The last cell closes the cursor, connection, and engine cleanly.

## What I Learned

The biggest shift from earlier days was thinking in SQL instead of pandas for the actual filtering and calculation -- Python's job here is mostly to hold the connection, pass the query string, and turn the result back into a DataFrame. Writing 50 queries back-to-back also made the different operator families click as a spectrum rather than isolated syntax: `IN` is really just shorthand for a chain of `OR`s on the same column, and `BETWEEN` is shorthand for two `AND`ed comparisons, so once the underlying logic was clear, choosing the "right" operator for each question got a lot faster.

Keeping credentials out of the notebook entirely -- loading them from `.env` with `python-dotenv` and raising a clear error if any are missing -- also made the whole thing feel more like real production code than a classroom exercise, since the notebook simply can't run with placeholder or missing secrets.

## Challenges Faced

The trickiest bug was in Q5, `SELECT ... age % 2 AS remainder`. Running it through `pd.read_sql_query()` threw a `TypeError: immutabledict is not a sequence` that had nothing to do with the SQL itself -- it turned out `psycopg2` treats `%` as a placeholder character for parameter substitution, so a literal modulo `%` in the query string confused it when no actual parameters were being passed. The fix was escaping it as `%%` in the query string, which was a good reminder that the same character can mean two completely different things depending on which layer of the stack is reading it.
