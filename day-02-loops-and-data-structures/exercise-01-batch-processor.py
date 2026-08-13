"""
Exercise: Batch Processor
Student: Nawaraj Tamang
Day: 2
"""

# Process batches 1 through 10
for batch_number in range(1, 11):
    # Show current batch being processed
    print(f"Processing batch {batch_number}")

    # Every third batch, show a checkpoint message
    if batch_number % 3 == 0:
        print("Checkpoint reached")