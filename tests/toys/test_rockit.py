import unittest
from src.toys.rockit import rockit


class TestRockit(unittest.TestCase):
    def test_rockit_returns_highest_index_for_greatest_frequency(self):
        self.assertEqual(rockit([10, 10, 7, 7, 7, 2, 7, 2]), 7)
        self.assertEqual(rockit([5, 5, 9, 19, 2, 2]), 1)
