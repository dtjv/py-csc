import unittest
import types
from src.toys.pipe import pipe


def add5(num):
    return num + 5


def sub2(num):
    return num - 2


class TestPipe(unittest.TestCase):
    def test_pipe_returns_a_function(self):
        f = pipe()
        self.assertIs(callable(f), True)
        self.assertIsInstance(f, types.FunctionType)

    def test_pipe(self):
        self.assertEqual(pipe(add5, sub2)(5), 8)
        self.assertEqual(pipe(add5, sub2, add5, sub2)(10), 16)
