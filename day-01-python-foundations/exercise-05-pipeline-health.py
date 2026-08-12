"""
Exercise: Pipeline Health
Student: Nawaraj Tamang
Day: 1
"""
#function to check pipeline health
def check_pipeline(rows_loaded, rows_failed, runtime_minutes):
    total_rows = rows_loaded + rows_failed
    failure_rate = (rows_failed / total_rows) * 100

    if failure_rate <= 2 and runtime_minutes <= 20:
        status = "Healthy"
    elif failure_rate <= 5:
        status = "Warning"
    else:
        status = "Critical"

    print(f"Failure rate: {failure_rate:.2f}%")
    print(f"Runtime: {runtime_minutes} minutes")
    print(f"Pipeline status: {status}")
    print("-" * 30)


# Test 1
check_pipeline(9800, 200, 18)

# Test 2
check_pipeline(9500, 500, 15)

# Test 3
check_pipeline(9900, 100, 30)