#!/usr/bin/python

import unittest
from math import sqrt


class Point:

    def __init__(self, x=0, y=0):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):              # zwraca string "(x, y)"
        return "(%s, %s)" % (self.x, self.y)

    def __repr__(self):             # zwraca string "Point(x, y)"
        return "Point(%s, %s)" % (self.x, self.y)

    def __eq__(self, other):        # obsluga point1 == point2
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __ne__(self, other):        # obsluga point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):       # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):       # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):       # v1 * v2, iloczyn skalarny
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):               # dlugosc wektora
        return sqrt(self.x * self.x + self.y * self.y)

# Kod testujacy modul.


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(10, 20)
        self.p2 = Point(20, 30)
        self.p3 = Point(30, 40)
        self.p4 = Point(10, 20)
        self.p5 = Point(4, -3)

    def test_str(self):
        self.assertEqual(str(self.p1), "(10, 20)")

    def test_repr(self):
        self.assertEqual(repr(self.p2), "Point(20, 30)")

    def test_eq(self):
        self.assertFalse(self.p1 == self.p2, False)
        self.assertTrue(self.p1 == self.p4, True)

    def test_ne(self):
        self.assertFalse(self.p1 != self.p4, False)
        self.assertTrue(self.p1 != self.p2, True)

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(30, 50))

    def test_sub(self):
        self.assertEqual(self.p3 - self.p1, Point(20, 20))

    def test_mul(self):
        self.assertEqual(self.p1 * self.p4, 500)

    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p3), -200)

    def test_length(self):
        self.assertEqual(self.p5.length(), 5)

    def tearDown(self):
        del self.p1
        del self.p2
        del self.p3
        del self.p4
        del self.p5

if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
