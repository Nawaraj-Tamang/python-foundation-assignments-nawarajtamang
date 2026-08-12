"""
Exercise: data quality checker
Student: Nawaraj Tamang
Day: 1
"""
#inputs
total_rows = 2000
missing_rows = 120
duplicate_rows = 30

#calculations
problematic_rows = missing_rows + duplicate_rows
problem_percentage = (problematic_rows / total_rows) * 100

if problem_percentage <= 2:
    classification = "Excellent"
elif problem_percentage <= 5:
    classification = "Acceptable"
else:
    classification = "Needs Cleaning"

#outputs
print(f"Total rows: {total_rows}")
print(f"Problematic rows: {problematic_rows}")
print(f"Problem percentage: {problem_percentage:.2f}%")
print(f"Final classification: {classification}")