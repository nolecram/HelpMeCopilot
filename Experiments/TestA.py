# function to convert a number to a binary string
import unittimport unittest
from TestA import to_binary

class TestToBinary(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (0, '0'),
            (1, '1'),
            (2, '10'),
            (3, '11'),
            (4, '100'),
            # Add more test cases as needed
        ]

    def test_to_binary(self):
        for input, expected_output in self.test_cases:
            self.assertEqual(to_binary(input), expected_output)

if __name__ == '__main__':
    unittest.main()
    # Importing the required unittest module
import unittest

# Importing the to_binary function from the TestA.py file
from TestA import to_binary

# Creating a class TestToBinary that inherits from unittest.TestCase
class TestToBinary(unittest.TestCase):
    # setUp method is overridden to set up the test environment before each test case
    # It initializes a list of test cases where each case is a tuple (input, expected_output)
    def setUp(self):
        self.test_cases = [
            (0, '0'),
            (1, '1'),
            (2, '10'),
            (3, '11'),
            (4, '100'),
            # Add more test cases as needed
        ]

    # test_to_binary is the test case method we are defining
    # It iterates over the test cases and for each one, it asserts if the to_binary function returns the expected output
    def test_to_binary(self):
        for input, expected_output in self.test_cases:
            self.assertEqual(to_binary(input), expected_output)

# The following line is the entry point to start the execution of unittests
if __name__ == '__main__':
    # Importing the required unittest module
import unittest

# Importing the to_binary function from the TestA.py file
from TestA import to_binary

# Creating a class TestToBinary that inherits from unittest.TestCase
class TestToBinary(unittest.TestCase):
    # setUp method is overridden to set up the test environment before each test case
    # It initializes a list of test cases where each case is a tuple (input, expected_output)
    def setUp(self):
        self.test_cases = [
            (0, '0'),
            (1, '1'),
            (2, '10'),
            (3, '11'),
            (4, '100'),
            # Add more test cases as needed
        ]

    # test_to_binary is the test case method we are defining
    # It iterates over the test cases and for each one, it asserts if the to_binary function returns the expected output
    def test_to_binary(self):
        for input, expected_output in self.test_cases:
            self.assertEqual(to_binary(input), expected_output)

# The following line is the entry point to start the execution of unittests
if __name__ == '__main__':
    unittest.main()    unittest.main()
