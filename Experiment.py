def convert_hours_to_minutes(hours):
    # convert hours to minutes
    minutes = hours * 60
    return minutes

# Ask the user for the duration of the movie in hours
hours = float(input("Enter the duration of the movie in hours: "))

# Convert the duration to minutes
minutes = convert_hours_to_minutes(hours)

print(f"The duration of the movie in minutes is: {minutes}")
def convert_celsius_to_fahrenheit(celsius):
    # formula to convert celsius to fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Ask the user for the temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))

# Convert the temperature to Fahrenheit
fahrenheit = convert_celsius_to_fahrenheit(celsius)

print(f"The temperature in Fahrenheit is: {fahrenheit}")
