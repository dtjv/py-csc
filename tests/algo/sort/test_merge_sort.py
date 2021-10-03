import unittest
from src.algo.sort.merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_handles_empty_array(self):
        self.assertEqual(merge_sort([]), [])

    def test_handles_array_of_one(self):
        self.assertEqual(merge_sort([10]), [10])

    def test_sorts_array_in_ascending_order(self):
        nums = [14, 33, 27, 10, 35, 19, 44, 42]
        actual = merge_sort(nums)
        expected = [10, 14, 19, 27, 33, 35, 42, 44]
        self.assertEqual(actual, expected)
