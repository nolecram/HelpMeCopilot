# Build a main function to calculate the duration of a movie in hours from the number of minutes
def main():
    minutes = int(input("How many minutes is the movie? "))
    hours = minutes // 60
    minutes = minutes % 60
    print("The movie is", hours, "hours and", minutes, "minutes long.")
main()