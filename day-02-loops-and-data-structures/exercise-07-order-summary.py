"""
Exercise: Nested Order Summary
Student: Nawaraj Tamang
Day: 2
"""

orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

# 1. Print every order ID and customer
print("All orders:")
for order_id, order_details in orders.items():
    print(f"{order_id}: {order_details['customer']}")

# 2. Print only completed orders
print("\nCompleted orders:")
for order_id, order_details in orders.items():
    if order_details["status"] == "Completed":
        print(f"{order_id}: {order_details['customer']} - NPR {order_details['amount']}")

# 3. Total amount of completed orders
completed_total = sum(
    order_details["amount"]
    for order_details in orders.values()
    if order_details["status"] == "Completed"
)

# 4. Count pending orders
pending_count = sum(
    1 for order_details in orders.values() if order_details["status"] == "Pending"
)

# 5. Add a new order to the dictionary
orders["ORD-004"] = {
    "customer": "Sagar",
    "amount": 1500,
    "status": "Pending"
}

# Output
print(f"\nTotal amount of completed orders: NPR {completed_total}")
print(f"Number of pending orders: {pending_count}")
print(f"\nUpdated orders dictionary: {orders}")