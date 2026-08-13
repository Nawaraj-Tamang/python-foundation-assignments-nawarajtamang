"""
Exercise: Retry Simulation
Student: Nawaraj Tamang
Day: 2
"""

# Retry settings
attempt = 1
max_attempts = 3
operation_successful = False

# Attempt the operation up to max_attempts times
while attempt <= max_attempts:
    print(f"Attempt {attempt}")

    # Stretch goal: simulate success on the second attempt
    if attempt == 2:
        operation_successful = True

    # Stop retrying early if the operation succeeded
    if operation_successful:
        break

    attempt += 1

# Report the final outcome
if operation_successful:
    print("Operation completed successfully")
else:
    print("Operation failed after three attempts")