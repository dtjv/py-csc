import unittest
from src.toys.ab_check import ab_check


class TestABCheck(unittest.TestCase):
    def test_should_not_find_pattern(self):
        self.assertIs(ab_check(), False)
        self.assertIs(ab_check('ab'), False)
        self.assertIs(ab_check('a....b'), False)

    def test_should_find_pattern(self):
        self.assertIs(ab_check('axxxb'), True)
        self.assertIs(ab_check('a123b'), True)
        self.assertIs(ab_check('bxxxa'), True)
        self.assertIs(ab_check('bxxxaababxa'), True)
