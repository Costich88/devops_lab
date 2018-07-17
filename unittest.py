#!/usr/bin/python3

# init test for task3
# demo

import task
import unittest


class TestTask(unittest.TestCase):

    def setup(self):
        """Init"""

    def test_input(self):
        self.assertEqual(task.fint("5 5"), [5, 5])
        self.assertEqual(task.fint("5, 5"), [5, 5])

    def test_foundsquare(self):
        self.assertEqual(task.find_square(2, 2), 4)
        self.assertEqual(task.find_square(3, 4), 12)

    def teardown(self):
        """Finish"""


if __name__ == '__main__':
    unittest.main()
