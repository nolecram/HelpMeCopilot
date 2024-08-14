# Build a function to convert a number to a binary number
def main():
    num = int(input("Enter a number: "))
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    print("The binary representation is", binary)
main()
