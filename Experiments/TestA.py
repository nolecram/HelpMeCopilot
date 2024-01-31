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