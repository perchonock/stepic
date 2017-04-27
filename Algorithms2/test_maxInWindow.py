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

    def test4(self):
        input = '15\n73 65 24 14 44 20 65 97 27 6 42 1 6 41 16\n7'
        output = getMax(input)
        self.assertTrue(output == '73 97 97 97 97 97 97 97 42', output)

    def test5(self):
        input = '15\n28 7 64 40 68 86 80 93 4 53 32 56 68 18 59\n12'
        output = getMax(input)
        self.assertTrue(output == '93 93 93 93', output)

    def test6(self):
        input = '15\n16 79 20 19 43 72 78 33 40 52 70 79 66 43 60\n12'
        output = getMax(input)
        self.assertTrue(output == '79 79 79 79', output)

    def test7(self):
        input = '15\n34 51 61 90 26 84 2 25 7 8 25 78 21 47 25\n3'
        output = getMax(input)
        self.assertTrue(output == '61 90 90 90 84 84 25 25 25 78 78 78 47', output)

    def test8(self):
        input = '15\n27 83 29 77 6 3 48 2 16 72 46 38 55 2 58 \n5'
        output = getMax(input)
        self.assertTrue(output == '83 83 77 77 48 72 72 72 72 72 58', output)