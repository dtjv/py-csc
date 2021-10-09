import unittest
import types
from src.toys import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fib_iterative(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21]

        for i in range(8):
            self.assertEqual(fibonacci.fib_iterative(i), expected[i])

    def test_fib_recursive(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21]

        for i in range(8):
            self.assertEqual(fibonacci.fib_recursive(i), expected[i])

    def test_fib_dp(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21]

        for i in range(8):
            self.assertEqual(fibonacci.fib_dp(i), expected[i])

    def test_fib_generator_is_a_generator_function(self):
        actual = type(fibonacci.fib_generator())
        expected = types.GeneratorType

        self.assertEqual(actual, expected)

    def test_fib_generator(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21]

        for i, n in enumerate(fibonacci.fib_generator()):
            self.assertEqual(n, expected[i])

            if i == len(expected) - 1:
                break
