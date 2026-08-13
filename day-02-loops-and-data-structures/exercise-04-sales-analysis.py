"""
Exercise: Sales List Analysis
Student: Nawaraj Tamang
Day: 2
"""

monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

# 1. Sorted list from highest to lowest
sorted_sales = sorted(monthly_sales, reverse=True)

# 2. Only values above 100000
high_sales = [amount for amount in monthly_sales if amount > 100000]

# 3. Each amount with 13% tax added
sales_with_tax = [amount * 1.13 for amount in monthly_sales]

# 4. Total sales amount
total_sales = sum(monthly_sales)

# 5. Average sales amount
average_sales = total_sales / len(monthly_sales)

# Output
print(f"Sorted (high to low): {sorted_sales}")
print(f"Above 100000: {high_sales}")
print(f"With 13% tax: {sales_with_tax}")
print(f"Total sales: NPR {total_sales:.2f}")
print(f"Average sales: NPR {average_sales:.2f}")