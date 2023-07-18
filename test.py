# function to convert a number to a binary string
def binary(n):
    if n == 0:
        return '0'
    else:
        return binary(n//2) + str(n%2)
    # Build a main function fro auser to input a number and get the binary string
def main():
    n = int(input("Enter a number: "))
    print(binary(n))
# Call the main function
main()
# Display a joke on python language
print("What do you call a bear with no teeth?\nA gummy bear!")


# Build a main function to calculate the duration of a movie in hours from minutes
def main():
    minutes = int(input("Enter the number of minutes: "))
    hours = minutes // 60
    remaining_minutes = minutes % 60
    print(minutes, "minutes is", hours, "hours and", remaining_minutes, "minutes")
# Call the main function
main()

# Build a test for the previous function
def test():
    print("Testing minutes_to_hours()...", end="")
    assert(minutes_to_hours(90) == "1 hour(s) and 30 minute(s)")
    assert(minutes_to_hours(0) == "0 hour(s) and 0 minute(s)")
    assert(minutes_to_hours(720) == "12 hour(s) and 0 minute(s)")
    print("Passed!")
    