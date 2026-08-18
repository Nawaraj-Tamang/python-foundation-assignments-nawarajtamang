# Day 3: Functions and Modules

## Topics Covered

- Default arguments
- `*args` (variable-length arguments)
- Multiple return values
- Built-in functions (`min`, `max`, `sum`, `sorted`)
- Variable scope and the `global` keyword
- Custom modules
- Standard library (`random`, `datetime`)

## Exercises

1. Simple Interest Calculator
2. Class Average
3. Analyze Numbers
4. Shared Booking Counter
5. Temperature Report Module

## How to Run

Run each file using:

```bash
python exercise-01-simple-interest-calculator.py
python exercise-02-class-average.py
python exercise-03-analyze-numbers.py
python exercise-04-booking-counter.py
python exercise-05-implementing-temperature-module.py
```

Exercise 5 also requires `temperature_utils.py` to be in the same folder, since the
script imports it directly.

## What I Learned

I learned how default arguments let a function stay flexible without forcing the caller
to pass every value every time, and how `*args` extends that idea further by accepting
any number of arguments at all, which is useful when I don't know in advance how many
values I'll get. I also practiced returning multiple values from a single function and
unpacking them into separate variables on the calling side, which is cleaner than
returning a dictionary or list when the values are logically distinct. Writing my own
module and importing it into another script showed me that custom code can be organized
and reused the exact same way as the standard library modules I've already been using,
like `random` and `datetime`.

## Challenges Faced

The trickiest part was understanding exactly when the `global` keyword is required.
At first I assumed any function could freely modify a variable defined outside it, but
Python actually treats a reassigned variable inside a function as local unless `global`
is explicitly used. This showed up directly in the booking counter exercise, where
`total_seats_booked += n` would have failed with an `UnboundLocalError` without the
`global` declaration, since `+=` both reads and reassigns the variable. I also ran into
a `SyntaxError` when I first named my module file with a hyphen (`temperature-utils.py`)
instead of an underscore, since Python reads a hyphen in an import statement as
subtraction rather than part of a name.
