from unittest import TestCase
from heap import *


class TestMaxInWindow(TestCase):
    def test1(self):
        l = 6
        arr = [0, 1, 2, 3, 4, 5]
        output = getShifts(arr)
        self.assertTrue(output == '0', output)

    def test2(self):
        l = 6
        arr = [7, 6, 5, 4, 3, 2]
        output = getShifts(arr)
        self.assertTrue(output == '4\n2 5\n1 4\n0 2\n2 5', output)