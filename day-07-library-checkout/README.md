# Day 7 -- Python for Data Engineering: Library Checkout Assignment

## Topics Covered

- Loading structured data into pandas with 'pd.read_csv()', including parsing date columns with 'parse_dates'
- Cleaning data column-by-column, choosing a different strategy for each based on what "missing" actually means (a boolean flag for one column, 'fillna(0)' for another)
- 'groupby()' and aggregation ('.mean()', '.sum()') to answer business questions, plus sorting results with '.sort_values()'
- Calling a real public HTTP API with the 'requests' library, checking the response with '.raise_for_status()', and parsing the returned JSON
- Wrapping an external API call in 'try'/'except' with a local fallback dictionary, so the pipeline stays resilient if the API is slow, down, or returns something unexpected
- Merging two DataFrames with 'pd.merge()' after reshaping one of them with '.reset_index()'

## Exercises

The assignment is delivered as a single notebook, 'Assignment_NawarajTamang.ipynb', with five problems building on Cedar Grove Public Library's checkout records in 'data/checkouts.csv':

1. **Load and get oriented** -- load the checkouts CSV with the three date columns parsed as real dates, then count total checkouts and how many are still outstanding.
2. **Clean the data, the right way for each column** -- add an 'is_returned' boolean column and fill missing 'late_fee' values with '0', since a missing checkout-related field means something different in each column.
3. **Which genre racks up the most late fees?** -- filter to returned books only, then find the average late fee per genre, sorted highest to lowest.
4. **Look up each book with a real public API** -- write 'get_book_facts()', which calls the Open Library search API for a book's author and first publish year, falling back to a local dictionary if the request fails, then run it for every title in the catalog.
5. **Which author costs the library the most in late fees?** -- merge the book facts into the checkout data and total the late fees per author.

This runs against my own 160-row 'data/checkouts.csv', tracking the library's twelve classic titles across checkout, due, and return dates, member IDs, and late fees.

## How to Run

This day uses a Jupyter notebook, not standalone '.py' scripts, so the workflow is different from the terminal-based days:

```bash
cd day-07-library-checkout
pip install -r requirements.txt
jupyter lab Assignment_NawarajTamang.ipynb
```

Open the notebook in VS Code (Jupyter extension, Python 3.13.3 kernel) or JupyterLab and run all cells top to bottom. Problem 4 calls the live Open Library API; if there's no internet connection, 'get_book_facts()' automatically falls back to the local 'BACKUP_BOOK_FACTS' dictionary, so every "check yourself" cell still passes either way.

## What I Learned

This assignment tied together the two biggest ideas from class: that real data almost never arrives clean, and that a missing value can mean completely different things depending on the column it's in. A missing 'return_date' isn't bad data at all -- it just means the book hasn't come back yet -- so instead of dropping those rows like I might have on an earlier day, I turned that into an explicit 'is_returned' flag. That felt like a much more honest way to represent the data than pretending every checkout has a return date.

Working with the Open Library API also made the 'try'/'except' fallback pattern click in a way it hadn't during Day 4's error-handling exercises. It's one thing to catch an exception in an isolated example; it's another to build a function that has to keep working even when a network call to a service I don't control fails partway through a loop over a dozen books. Wrapping the request, the JSON parsing, and the fallback lookup all in the same 'try' block, and catching 'RequestException', 'KeyError', and 'IndexError' together, made the difference between a script that crashes on one bad title and one that just quietly recovers.

## Challenges Faced

The main challenge was Problem 5's merge. 'book_facts_df' came back indexed by 'book_title' rather than having it as a normal column, so merging it straight into 'checkouts_clean' on that column failed until I remembered to call '.reset_index()' first to turn the index back into a column pandas could actually join on.
