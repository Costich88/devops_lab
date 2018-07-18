#!/usr/bin/python3

# init test for task3
# demo

import task
import unittest


class TestTask(unittest.TestCase):

    def setup(self):
        """Init"""

    def test_input(self):
        self.assertEqual(task.fint('5 5'), [5, 5])
        self.assertEqual(task.fint('5  5'), [5, 5])

    def test_foundsquare(self):
        self.assertEqual(task.findsquare(2, 2), 4)
        self.assertEqual(task.findsquare(3, 4), 12)

    def test_squarearray(self):
        self.assertEqual(task.squarearray(3, 2), [[0, 0], [0, 0], [0, 0]])

    def test_cutsqaure(self):
        self.assertEqual(task.cutsqaure(0, 0, 2, 2, [[0, 0], [0, 0], [0, 0]]),
                         [[1, 1], [1, 1], [0, 0]])

    def test_totcutted(self):
        self.assertEqual(task.totcutted([[1, 1], [1, 1], [0, 0]]), 4)

    def paintersquare(self):
        self.assertEqual(task.paintersquare('2 3', [['0 0 2 2']]), 2)

    def teardown(self):
        """Finish"""


if __name__ == '__main__':
    unittest.main()
