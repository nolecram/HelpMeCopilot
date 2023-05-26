# build a main function to collect celsius and convert to fahrenheit
def main():
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
main()

# build a unit test function to test the main function
def test():
    assert main() == 32
    return "pass"
test()
