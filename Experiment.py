def convert_duration(duration_in_minutes):
    hours = duration_in_minutes // 60
    minutes = duration_in_minutes % 60
    return f"{hours} hours and {minutes} minutes"

# Test the function
print(convert_duration(120))  # Output: 2 hours and 0 minutes
print(convert_duration(90))   # Output: 1 hours and 30 minutes
