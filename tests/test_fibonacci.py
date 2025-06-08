# This file will contain tests for the Fibonacci function.
import unittest
# We will need to adjust the import path later if necessary,
# depending on how the project is structured and run.
from fibonacci.fibonacci import calculate_fibonacci

class TestFibonacci(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(calculate_fibonacci(0), 0)

    def test_one(self):
        self.assertEqual(calculate_fibonacci(1), 1)

    def test_positive_numbers(self):
        self.assertEqual(calculate_fibonacci(2), 1)
        self.assertEqual(calculate_fibonacci(3), 2)
        self.assertEqual(calculate_fibonacci(10), 55)
        self.assertEqual(calculate_fibonacci(20), 6765)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            calculate_fibonacci(-1)
        with self.assertRaises(ValueError):
            calculate_fibonacci(-5)

if __name__ == '__main__':
    unittest.main()
