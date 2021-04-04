import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    def test_new_stack_is_empty(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)

    def test_push_adds_to_stack(self):
        stack = Stack()
        stack.push(3)
        stack.push(4)
        self.assertEqual(len(stack), 2)

    def test_pop_removes_from_stack(self):
        stack = Stack()
        stack.push(3)
        stack.push(4)
        stack.pop()
        self.assertEqual(len(stack), 1)

    def test_last_in_first_out(self):
        stack = Stack()
        stack.push(3)
        stack.push(4)
        result = stack.pop()
        self.assertEqual(result, 4)

    def test_pop_on_empty_stack(self):
        stack = Stack()
        self.assertIsNone(stack.pop())

    def test_stack_is_iterable(self):
        stack = Stack()
        stack.push(2)
        stack.push(1)
        stack.push(0)

        for i, item in enumerate(stack):
            self.assertEqual(item, i)
