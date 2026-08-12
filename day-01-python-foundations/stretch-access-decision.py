def check_access(user_role, is_active, requested_dataset):
    allowed_roles = ["analyst", "scientist", "engineer"]
    restricted_datasets = ["salary_data", "personal_data"]

    if not is_active:
        print("Access denied because the user is inactive.")
    elif user_role not in allowed_roles:
        print("Access denied because the role is not allowed.")
    elif requested_dataset in restricted_datasets:
        print("Access denied because the dataset is restricted.")
    else:
        print(f"Access granted to '{requested_dataset}' for role '{user_role}'.")

    print("-" * 40)


# Test 1: everything checks out
check_access("analyst", True, "sales_data")

# Test 2: user is inactive
check_access("analyst", False, "sales_data")

# Test 3: role not allowed
check_access("intern", True, "sales_data")

# Test 4: dataset is restricted
check_access("scientist", True, "salary_data")