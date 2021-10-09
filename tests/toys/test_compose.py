import unittest
import types
from src.toys.compose import compose


def say_hi(name, *_):
    return "hi" + " " + name


def yell(statement, *_):
    return statement.upper() + "!"


class TestCompose(unittest.TestCase):
    def test_compose_returns_a_function(self):
        f = compose()
        self.assertIs(callable(f), True)
        self.assertIsInstance(f, types.FunctionType)

    def test_compose(self):
        self.assertEqual(compose(say_hi, yell)("joe"), "hi JOE!")
