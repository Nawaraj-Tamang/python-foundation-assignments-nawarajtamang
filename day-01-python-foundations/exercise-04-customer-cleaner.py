"""
Exercise: Customer Cleaner
Student: Nawaraj Tamang
Day: 1
"""
#inputs
raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

#operations
name = raw_name.strip().title()
city = raw_city.strip().title()
age = int(raw_age.strip())
email = raw_email.strip().lower()

status = "Adult" if age >= 18 else "Minor"

#outputs
print(f"Name: {name}")
print(f"City: {city}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Status: {status}")