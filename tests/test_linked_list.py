import unittest
from src.linked_list import LinkedList


def setup():
    data = list(range(1, 5))
    linked_list = LinkedList()

    for num in data:
        linked_list.add(num)

    return data, linked_list


class TestStack(unittest.TestCase):
    def test_len_returns_list_length(self):
        data, ll = setup()

        self.assertEqual(len(ll), len(data))

    def test_add_value_to_list(self):
        data, ll = setup()
        values = [ll.get_value_at_index(idx) for idx in range(len(ll))]

        self.assertEqual(values, data)

    def test_remove_a_value_from_list(self):
        data, ll = setup()

        ll.remove(2)
        data.remove(2)

        values = [ll.get_value_at_index(idx) for idx in range(len(ll))]

        self.assertEqual(values, data)

    def test_reverse_list(self):
        data, ll = setup()

        ll.reverse()
        data.reverse()

        values = [ll.get_value_at_index(idx) for idx in range(len(ll))]

        self.assertEqual(values, data)
