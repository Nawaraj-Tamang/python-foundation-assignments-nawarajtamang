"""
Exercise: File Validator
Student: Nawaraj Tamang
Day: 1
"""
#inputs
file_name = input("Enter a file name: ")
file_name = file_name.strip().lower()

valid_extensions = (".csv", ".json", ".parquet")

#outputs
if file_name.endswith(valid_extensions):
    print(f"'{file_name}' is a valid file type. ✅")
else:
    print(f"'{file_name}' is NOT a valid file type. ❌")