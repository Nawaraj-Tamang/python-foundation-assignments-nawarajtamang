"""
Exercise: Dataset Comparison
Student: Nawaraj Tamang
Day: 2
"""

dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

# All unique dataset names (combined, no duplicates)
all_datasets = dataset_a | dataset_b

# Datasets found in both groups
common_datasets = dataset_a & dataset_b

# Datasets only in dataset_a
only_in_a = dataset_a - dataset_b

# Datasets only in dataset_b
only_in_b = dataset_b - dataset_a

# Output
print(f"All unique datasets: {all_datasets}")
print(f"Common to both: {common_datasets}")
print(f"Only in dataset_a: {only_in_a}")
print(f"Only in dataset_b: {only_in_b}")