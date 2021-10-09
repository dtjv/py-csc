import unittest
from src.toys.encode_string import encode_string


class TestEncodeString(unittest.TestCase):
    def test_should_return_empty_string(self):
        self.assertEqual(encode_string(), '')
        self.assertEqual(encode_string(''), '')
        self.assertEqual(encode_string('aeiou'), '')

    def test_should_remove_vowels(self):
        self.assertEqual(encode_string('baeiou'), 'c')

    def test_should_remove_duplicates(self):
        self.assertEqual(encode_string('bbb'), 'c')

    def test_should_encode_string(self):
        self.assertEqual(encode_string('bcd'), 'dfe')
        self.assertEqual(encode_string('auzepizzomuo'), 'obl')
