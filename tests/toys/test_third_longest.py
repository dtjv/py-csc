import unittest
from src.toys.third_longest import third_longest


class TestThirdLongest(unittest.TestCase):
    def test_handles_no_input(self):
        self.assertEqual(third_longest(), '')

    def test_should_return_third_longest(self):
        self.assertEqual(third_longest(['aaa', 'bb', 'c']), 'c')
