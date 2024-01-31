def to_binary(n):
    return bin(n)[2:]

def test_to_binary():
    # Test case 1: Positive number
    assert to_binary(10) == "1010"

    # Test case 2: Negative number
    assert to_binary(-10) == "-1010"

    # Test case 3: Zero
    assert to_binary(0) == "0"

    # Test case 4: Large positive number
    assert to_binary(1234567890) == "1001001100101100000001011010010"

    # Test case 5: Large negative number
    assert to_binary(-1234567890) == "-1001001100101100000001011010010"

    print("All test cases passed!")

test_to_binary()