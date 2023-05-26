# function to convert a number to a binary string
def to_binary(n):
    return bin(n)[2:]
# Build a main function for a user to input a number and get the binary string
def main():
    n = int(input("Enter a number: "))
    print(to_binary(n))
# build a unit test function to test the main function
def test():
    assert main() == 1
    return "pass"
test()
# Call the main function
main()
# Display a joke on python language that I not like
print("Why did the python cross the road? To escape the snake charmer!")