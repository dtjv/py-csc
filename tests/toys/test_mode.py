import unittest
from src.toys.mode import mode


class TestMode(unittest.TestCase):
    def test_handles_no_input(self):
        self.assertEqual(mode([]), -1)

    def test_should_return_third_longest(self):
        self.assertEqual(mode([1, 2, 3, 3, 2, 1, 4, 3]), 3)
