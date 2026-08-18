"""
Exercise: Class Average Using *args
Student: Nawaraj Tamang
Day: 3
"""

# Calculation of class average using *args

def class_average(*scores):
    #edge case: no scores passed
    if len(scores) == 0:
        return 0

    #calculation
    average = sum(scores) / len(scores)
    return round(average, 2)


# output
print(class_average(80, 90, 70))
print(class_average(55, 60, 65, 70, 75))
print(class_average())