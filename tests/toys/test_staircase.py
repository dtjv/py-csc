import unittest
from src.toys.staircase import staircase


class TestStaircase(unittest.TestCase):
    def test_should_return_a_string(self):
        self.assertIsInstance(staircase(5), str)

    def test_should_return_n_steps(self):
        steps = staircase(4).split('\n')
        self.assertEqual(len(steps), 4)

    def test_should_ascend_by_one_each_step(self):
        steps = staircase(4).split('\n')

        for idx, step in enumerate(steps):
            self.assertEqual(len(step.lstrip()), idx + 1)
