from unittest import TestCase
from maxInWindow import *


class TestMaxInWindow(TestCase):
    def test1(self):
        input = '3\n2 1 5\n1'
        output = getMax(input)
        self.assertTrue(output == '2 1 5', output)

    def test2(self):
        input = '8\n2 7 3 1 5 2 6 2\n4'
        output = getMax(input)
        self.assertTrue(output == '7 7 5 6 6', output)

    def test2(self):
        input = '8\n2 7 3 1 5 2 6 2\n4'
        output = getMax(input)
        self.assertTrue(output == '7 7 5 6 6', output)

    def test3(self):
        input = '3\n2 3 9\n3'
        output = getMax(input)
        self.assertTrue(output == '9', output)

