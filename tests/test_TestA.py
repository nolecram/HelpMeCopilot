# Build a function to convert a number to a binary number
def convert_to_binary(num):
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

# Test function for pytest
def test_convert_to_binary():
    assert convert_to_binary(5) == "101"
    assert convert_to_binary(0) == ""
    assert convert_to_binary(10) == "1010"
    assert convert_to_binary(1) == "1"