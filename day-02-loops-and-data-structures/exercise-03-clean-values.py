"""
Exercise: Clean Numeric Values
Student:Nawaraj Tamang
Day: 2
"""
# using loop
print("Using loop:")
raw_values = [100, None, 250, "invalid", 300, None, 450]

# Build a list of only valid integers
clean_values = []

for value in raw_values:
    # Skip anything that isn't strictly an int
    if not isinstance(value, int):
        continue
    clean_values.append(value)

print(clean_values)

print("----------------------------")

#using list comprehension
print("Using list comprehension:")
raw_values = [100, None, 250, "invalid", 300, None, 450]

# Filter for valid integers in one line
clean_values = [value for value in raw_values if isinstance(value, int)]

print(clean_values)