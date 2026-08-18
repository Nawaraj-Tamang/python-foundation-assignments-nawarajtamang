"""
Exercise: Analyze Numbers (Multiple Return Values + Built-ins)
Student: Nawaraj Tamang
Day: 3
"""

# Calculation of smallest, largest, total and descending order of numbers using built-ins

def analyze_numbers(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    total = sum(numbers)
    desc = sorted(numbers, reverse=True)

    return smallest, largest, total, desc


# outputs
smallest, largest, total, desc = analyze_numbers([4, 9, 1, 7, 3])
print(smallest)
print(largest)
print(total)
print(desc)

smallest, largest, total, desc = analyze_numbers([10, 20, 30, 40, 50])
print(smallest)
print(largest)
print(total)
print(desc)