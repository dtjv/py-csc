import unittest
from src.toys.factorial import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        expected = [1, 1, 2, 6, 24, 120]

        for i in range(len(expected)):
            self.assertEqual(factorial(i), expected[i])
