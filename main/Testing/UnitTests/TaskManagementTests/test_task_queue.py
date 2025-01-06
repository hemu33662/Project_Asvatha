import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from Core.TaskManagement.task_queue import TaskQueue


class TestTaskQueue(unittest.TestCase):
    def setUp(self):
        self.queue = TaskQueue()

    def test_add_task(self):
        task = "open Paint"
        self.queue.add_task(task)
        self.assertEqual(self.queue.process_task(), task)

    def test_empty_queue(self):
        self.assertIsNone(self.queue.process_task())

    def test_cancel_task(self):
        task = "open chrome"
        self.queue.add_task(task)
        self.queue.cancel_task(task)
        self.assertIsNone(self.queue.process_task())

    def test_callable_task(self):
        # A simple function to test task execution
        def test_function():
            print("Test function executed")

        self.queue.add_task(test_function)
        self.queue.process_task()  # Expect "Test function executed" to be printed

if __name__ == "__main__":
    unittest.main()
