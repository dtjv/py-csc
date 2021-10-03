import unittest
from src.algo.sort.selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    def test_handles_empty_array(self):
        self.assertEqual(selection_sort([]), [])

    def test_handles_array_of_one(self):
        self.assertEqual(selection_sort([10]), [10])

    def test_sorts_array_in_ascending_order(self):
        nums = [14, 33, 27, 10, 35, 19, 44, 42]
        actual = selection_sort(nums)
        expected = [10, 14, 19, 27, 33, 35, 42, 44]
        self.assertEqual(actual, expected)

    def test_sorts_array_in_place(self):
        nums = [14, 33, 27, 10, 35, 19, 44, 42]
        result = selection_sort(nums)
        self.assertIs(nums, result)
