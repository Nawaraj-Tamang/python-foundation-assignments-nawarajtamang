# Day 2: Loops, Comprehensions, and Data Structures

## Topics Covered

- `for` loops and `range()`
- `while` loops and `break`
- `continue` and `isinstance()`
- List comprehensions
- Set operations (union, intersection, difference)
- Dictionaries and dictionary comprehensions
- Nested dictionaries
- Building an interactive menu-driven program with `input()`

## Exercises

1. Batch Processor
2. Retry Simulation
3. Clean Numeric Values
4. Sales List Analysis
5. Dataset Comparison
6. Student Score Dictionary
7. Nested Order Summary
8. Contact Book Menu (Stretch)

## How to Run

Run each file using:

```bash
python exercise-01-batch-processor.py
```

Replace the filename with the exercise you want to run, for example:

```bash
python exercise-08-contact-book-menu.py
```

## What I Learned

Today I learned how loops and comprehensions let me process collections more efficiently than writing everything out manually. `for` loops with `range()` and the modulo operator were useful for detecting patterns like every third item, while `while` loops combined with `break` gave me more control over stopping a process early, such as ending retries once an operation succeeds. I also learned how set operations (`|`, `&`, `-`) make comparing two collections much simpler than writing manual loops with `if item in other_set` checks, and how nested dictionaries let me model more realistic, structured data like orders and contacts with multiple fields each.

## Challenges Faced

The trickiest part was working with nested dictionaries in the Order Summary and Contact Book exercises, since I had to remember to access an inner key (like `order_details["amount"]`) rather than treating each value as a single number. I also had to be careful with the Contact Book exercise to check `if name in contacts` before searching or deleting, since trying to access or remove a key that doesn't exist would otherwise crash the program with a `KeyError`. Writing the checks before performing the action, rather than after, fixed this and kept the program running smoothly no matter what the user typed in.
