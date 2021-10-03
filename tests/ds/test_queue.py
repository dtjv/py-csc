import unittest
from src.ds.queue import Queue


class TestQueue(unittest.TestCase):
    def test_new_queue_is_empty(self):
        queue = Queue()
        self.assertEqual(len(queue), 0)

    def test_enqueue_adds_to_queue(self):
        queue = Queue()
        queue.enqueue(3)
        queue.enqueue(4)
        self.assertEqual(len(queue), 2)

    def test_dequeue_removes_from_queue(self):
        queue = Queue()
        queue.enqueue(3)
        queue.enqueue(4)
        queue.dequeue()
        self.assertEqual(len(queue), 1)

    def test_first_in_first_out(self):
        queue = Queue()
        queue.enqueue(3)
        queue.enqueue(4)
        queue.dequeue()
        queue.enqueue(8)
        queue.enqueue(9)
        queue.dequeue()
        result = queue.dequeue()
        self.assertEqual(result, 8)

    def test_dequeue_on_empty_queue(self):
        queue = Queue()
        self.assertIsNone(queue.dequeue())
