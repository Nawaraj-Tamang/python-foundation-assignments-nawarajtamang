# Day 4: File Handling, Error Handling & Logging

## Topics Covered

- File handling (read/write, 'with' statement)
- CSV module ('csv.DictReader', 'csv.writer')
- JSON module ('json.load', 'json.dump')
- Custom exceptions
- Error handling ('try' / 'except' / 'else' / 'finally')
- Logging ('logging' module, 'FileHandler', log levels)

## Exercises

All 5 exercises are contained in a single notebook, 'exercises.ipynb':

1. Line & Word Counter
2. Inventory Value from CSV
3. Filtering a JSON Library Catalog
4. Custom Exception for User Registration
5. Order Pipeline with Logging

## How to Run

Open 'exercises.ipynb' in VS Code with the Jupyter extension installed, then run the cells in order from top to bottom (either cell-by-cell with the play button, or via **Run All**). Each question has a **setup cell** (creates the sample data file it needs — 'diary.txt', 'products.csv', 'library.json', or 'orders.csv') followed by an **answer cell**, so setup cells must be run before the corresponding answer cell.

## What I Learned

This day connected several pieces that had been separate before: reading and writing files safely with 'with open(...)', parsing structured data with 'csv.DictReader' and 'json.load'/'json.dump', and handling failures gracefully instead of letting a script crash. I learned that data coming from a CSV is always read as strings, so numeric conversion has to be done explicitly before any calculation. Working through custom exceptions showed me how subclassing 'Exception' lets me raise errors that describe my own business rules (like an invalid age) rather than relying only on Python's built-in error types, and how 'try/except/else' separates the "what if it fails" logic from the "what happens on success" logic cleanly. The logging exercise tied everything together — instead of using 'print()' to track what went wrong in a row-by-row CSV pipeline, I used 'logging.getLogger()' with a 'FileHandler' to write timestamped 'INFO', 'ERROR', and 'CRITICAL' messages to a log file, which is much closer to how a real data pipeline would report problems.

## Challenges Faced

The trickiest part was the Order Pipeline exercise, specifically making sure invalid rows were logged and skipped without stopping the rest of the file from being processed. My first attempt let one bad row (a non-numeric 'qty') raise a 'ValueError' that killed the whole loop. I fixed this by wrapping just the conversion step for each row in its own 'try/except ValueError', using 'continue' to move to the next row instead of exiting the function. I also ran into duplicate log entries the second time I reran the notebook, since 'logging.getLogger("orders")' returns the same logger object across calls and handlers stack up if you keep adding them. Calling 'logger.handlers.clear()' before adding a new 'FileHandler' solved that.
