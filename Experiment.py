# Build a program to convert the duration of a movie in seconds to hours, minutes, and seconds.
# Build the main function to collect the duration of the movie in seconds.
def main():
    # Collect the duration of the movie in seconds.
    duration = int(input("Enter the duration of the movie in seconds: "))
    # Call the convert function to convert the duration of the movie in seconds to hours, minutes, and seconds.
    convert(duration)
# Build the convert function to convert the duration of the movie in seconds to hours, minutes, and seconds.
def convert(duration):
    # Calculate the hours, minutes, and seconds of the movie.
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = (duration % 3600) % 60
    # Display the hours, minutes, and seconds of the movie.
    print("The duration of the movie is", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")
# Call the main function.
main()
# End of program