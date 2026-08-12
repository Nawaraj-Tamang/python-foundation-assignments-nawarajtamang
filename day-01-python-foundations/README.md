# Day 1: Python Foundations

## Topics Covered

- Variables
- Data types
- String methods
- Operators
- Conditional statements

## Exercises

1. Sales Summary
2. Data Quality Checker
3. File Validator
4. Customer Record Cleaner
5. Pipeline Health Status
6. Dataset Access Decision

## How to Run

Run each file using:

```bash
python exercise-01-sales-summary.py
python exercise-02-data-quality-checker.py
python exercise-03-file-validator.py
python exercise-04-customer-record-cleaner.py
python exercise-05-pipeline-health-status.py
python exercise-06-dataset-access-decision.py
```

## What I Learned

I learned how to clean and standardize messy input data using string methods like `.strip()`, `.lower()`, and `.title()`, and how f-strings with format specifiers (like `:.2f`) make output much more readable. I also practiced writing conditional logic with `if/elif/else` and ternary expressions to classify data based on multiple thresholds, and saw how combining conditions with `and` can change the outcome significantly compared to checking them separately.

## Challenges Faced

The trickiest part was the Pipeline Health Status exercise, specifically the case where the failure rate was low but the runtime was high. Initially it seemed like it should count as "Healthy" since the failure rate alone met the threshold, but I realized the rules required both conditions to hold, not just one. I solved this by using `and` in the condition (`failure_rate <= 2 and runtime_minutes <= 20`) instead of checking failure rate alone, which correctly pushed that case down into "Warning."
