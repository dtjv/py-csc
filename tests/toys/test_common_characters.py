import unittest
from src.toys.common_characters import common_characters


class TestCommonCharacters(unittest.TestCase):
    def test_no_args(self):
        self.assertEqual(common_characters(), '')

    def test_one_arg(self):
        self.assertEqual(common_characters('abc'), 'abc')

    def test_no_common_characters_found(self):
        self.assertEqual(common_characters('abc', 'xyz'), '')
        self.assertEqual(common_characters('abc', 'xyz', '123'), '')

    def test_common_characters_found(self):
        self.assertEqual(
            common_characters(
                'acex ivou',
                'aegihobu',
                'xxaybe ppic owu'),
            'aeiou')

    def test_skips_spaces(self):
        self.assertEqual(
            common_characters(
                'ab c',
                ' bc',
                'ca b'),
            'bc')

    def test_skips_chars_previously_encountered(self):
        self.assertEqual(
            common_characters(
                'abbcc',
                ' bc',
                'ca b'),
            'bc')
