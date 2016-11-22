#!/usr/bin/python

import unittest
from fractions import gcd


class Frac:

    def __init__(self, x=0, y=1):
        self.x = x / gcd(x, y)
        self.y = y / gcd(x, y)

    # skrocenie ulamka, np. [2, 4] -> [1, 2]
    def reduce_frac(self):
        self.validate_frac()
        return Frac(self.x / gcd(self.x, self.y), self.y / gcd(self.x, self.y))

    # sprawdz czy ulamek jest poprawny
    def validate_frac(self):
        if self.y == 0:
            raise Exception("Invalid fraction")

    def __str__(self):              # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return "%s" % self.x
        else:
            return "%s/%s" % (self.x, self.y)

    def __repr__(self):             # zwraca "Frac(x, y)"
        return "Frac(%s, %s)" % (self.x, self.y)

    def __add__(self, other):       # frac1 + frac2
        self.validate_frac()
        other.validate_frac()

        if self.y == other.y:
            return Frac(self.x + other.x, self.y)

        frac1_temp = [self.x * other.y, self.y * other.y]
        frac2_temp = [other.x * self.y, other.y * self.y]

        return Frac(frac1_temp[0] + frac2_temp[0], frac1_temp[1])

    def __sub__(self, other):       # frac1 - frac2
        self.validate_frac()
        other.validate_frac()

        if self.y == other.y:
            return Frac(self.x - other.x, self.y)

        frac1_temp = [self.x * other.y, self.y * other.y]
        frac2_temp = [other.x * self.y, other.y * self.y]

        return Frac(frac1_temp[0] - frac2_temp[0], frac1_temp[1])

    def __mul__(self, other):       # frac1 * frac2
        self.validate_frac()
        other.validate_frac()
        return Frac(self.x * other.x, self.y * other.y)

    def __div__(self, other):   # frac1 / frac2
        self.validate_frac()
        other.validate_frac()

        if other.x == 0:
            raise ZeroDivisionError

        return Frac(self.x * other.y, self.y * other.x)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __cmp__(self, other):       # cmp(frac1, frac2)
        self.validate_frac()
        other.validate_frac()

        self.reduce_frac()
        other.reduce_frac()

        if self.x == other.x and self.y == other.y:
            return 0

        frac1_temp = Frac(self.x * other.y, self.y * other.y)
        frac2_temp = Frac(other.x * self.y, other.y * self.y)

        return 1 if frac1_temp.x > frac2_temp.x else -1

    def __float__(self):            # float(frac)
        self.validate_frac()
        return float(self.x) / self.y

# Kod testujacy modul.


class TestFrac(unittest.TestCase):

    def setUp(self):
        self.zero = Frac(0, 1)

    def test_reduce_frac(self):
        self.assertEqual(Frac(2, 4).reduce_frac(), Frac(1, 2))

    def test_validate_frac(self):
        self.assertRaises(Exception, Frac.validate_frac, Frac(2, 0))

    def test_add_frac(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(2, 4) + Frac(3, 4), Frac(5, 4))
        self.assertRaises(Exception, Frac.__add__, Frac(1, 0), Frac(1, 3))

    def test_sub_frac(self):
        self.assertEqual(Frac(2, 3) - Frac(1, 2), Frac(1, 6))
        self.assertEqual(Frac(1, 2) - Frac(1, 2), self.zero)
        self.assertRaises(Exception, Frac.__sub__, Frac(2, 0), Frac(1, 2))

    def test_mul_frac(self):
        self.assertEqual(Frac(2, 3) * Frac(3, 4), Frac(1, 2))
        self.assertEqual(Frac(6, 1) * Frac(3, 4), Frac(9, 2))
        self.assertRaises(Exception, Frac.__mul__, Frac(2, 3), Frac(3, 0))

    def test_div_frac(self):
        self.assertEqual(Frac(1, 2) / Frac(3, 4), Frac(2, 3))
        self.assertEqual(Frac(3, 2) / Frac(1, 2), Frac(3, 1))
        self.assertRaises(ZeroDivisionError, Frac.__div__, Frac(1, 2), self.zero)
        self.assertRaises(Exception, Frac.__div__, Frac(1, 2), Frac(1, 0))
        self.assertRaises(Exception, Frac.__div__, Frac(1, 0), Frac(1, 4))

    def test_neg_frac(self):
        self.assertEqual(-Frac(1, 2), Frac(-1, 2))

    def test_invert_frac(self):
        self.assertEqual(Frac(1, 2).__invert__(), Frac(2, 1))

    def test_cmp_frac(self):
        self.assertEqual(Frac(2, 3).__cmp__(Frac(1, 2)), 1)
        self.assertEqual(Frac(4, 17).__cmp__(Frac(5, 18)), -1)
        self.assertEqual(Frac(2, 4).__cmp__(Frac(1, 2)), 0)
        self.assertRaises(Exception, Frac(2, 4).__cmp__, Frac(1, 0))

    def test_frac2float(self):
        self.assertEqual(float(Frac(3, 4)), 0.75)
        self.assertEqual(float(Frac(4, 8)), 0.5)
        self.assertRaises(Exception, Frac.__float__, Frac(2, 0))

    def tearDown(self):
        del self.zero


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
