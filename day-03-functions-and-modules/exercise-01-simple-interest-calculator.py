"""
Exercise: Simple Interest Calculator (Default Arguments)
Student: Nawaraj Tamang
Day: 3
"""

# Calculation of simple interest using default arguments

def calculate_simple_interest(principal, rate=5, time=1):
    interest = (principal * rate * time) / 100
    return interest


# output
print(calculate_simple_interest(1000, 10, 2))
print(calculate_simple_interest(1000))
print(calculate_simple_interest(2000, time=3))