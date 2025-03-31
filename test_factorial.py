import unittest
from testing_completion import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_base_cases(self):
        self.assertEqual(factorial(0), 0)
        self.assertEqual(factorial(1), 1)
    
    def test_factorial_positive_numbers(self):
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)
    
    def test_factorial_memoization(self):
        # Test that memoization works by calling the same value twice
        first_call = factorial(6)
        second_call = factorial(6)
        self.assertEqual(first_call, second_call)
        self.assertEqual(first_call, 720)

if __name__ == '__main__':
    unittest.main()