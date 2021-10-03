import unittest
from src.algo.search.binary_search import binary_search_iterative
from src.algo.search.binary_search import binary_search_recursive


class TestBinarySearchIterative(unittest.TestCase):
    def test_finds_target_index_for_even_length_list(self):
        collection = [0, 1, 2, 3, 4, 5]

        for idx, target in enumerate(collection):
            self.assertEqual(binary_search_iterative(target, collection), idx)

    def test_finds_target_index_for_odd_length_list(self):
        collection = [0, 1, 2, 3, 4]

        for idx, target in enumerate(collection):
            self.assertEqual(binary_search_iterative(target, collection), idx)

    def test_target_not_found(self):
        collection = [1, 3, 5]
        targets = [0, 2, 4, 6]

        for target in targets:
            self.assertEqual(binary_search_iterative(target, collection), -1)


class TestBinarySearchRecursive(unittest.TestCase):
    def test_finds_target_index_for_even_length_list(self):
        collection = [0, 1, 2, 3, 4, 5]

        for idx, target in enumerate(collection):
            self.assertEqual(binary_search_recursive(target, collection), idx)

    def test_finds_target_index_for_odd_length_list(self):
        collection = [0, 1, 2, 3, 4]

        for idx, target in enumerate(collection):
            self.assertEqual(binary_search_recursive(target, collection), idx)

    def test_target_not_found(self):
        collection = [1, 3, 5]
        targets = [0, 2, 4, 6]

        for target in targets:
            self.assertEqual(binary_search_recursive(target, collection), -1)
