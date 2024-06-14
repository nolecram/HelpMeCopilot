def convert_hours_to_minutes(hours):
    # convert hours to minutes
    minutes = hours * 60
    return minutes

# Ask the user for the duration of the movie in hours
hours = float(input("Enter the duration of the movie in hours: "))

# Convert the duration to minutes
minutes = convert_hours_to_minutes(hours)

print(f"The duration of the movie in minutes is: {minutes}")
