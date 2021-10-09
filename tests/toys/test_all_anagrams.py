import unittest
from src.toys.all_anagrams import all_anagrams


class TestABCheck(unittest.TestCase):
    def test_should_return_all_permutations_without_repetition(self):
        self.assertEqual(
            all_anagrams('abc'), [
                'abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
