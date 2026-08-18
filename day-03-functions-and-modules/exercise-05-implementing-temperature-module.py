"""
Exercise: Temperature Report Module (Custom Module + Standard Library)
Student: Nawaraj Tamang
Day: 3
"""

# Part B

import random
import datetime
import temperature_utils

# 1. generate 5 random Celsius temperatures between 15 and 40 (inclusive)
celsius_temps = [random.randint(15, 40) for _ in range(5)]

# 2. convert each to Fahrenheit using your module
fahrenheit_temps = [temperature_utils.celsius_to_fahrenheit(c) for c in celsius_temps]

# 3. print today's date in the format: Temperature Report — DD-MM-YYYY
today = datetime.date.today()
print(f"Temperature Report — {today.strftime('%d-%m-%Y')}")

# 4. print the Celsius list, the Fahrenheit list, and the module version
print(f"Celsius:    {celsius_temps}")
print(f"Fahrenheit: {fahrenheit_temps}")
print(f"Module version: {temperature_utils.MODULE_VERSION}")