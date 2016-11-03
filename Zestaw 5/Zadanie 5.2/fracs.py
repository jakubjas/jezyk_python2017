#!/usr/bin/python

import unittest
from fractions import gcd


# sprawdz czy ulamek jest poprawny
def validate_frac(frac):

    if frac[1] == 0:
        raise Exception("Invalid fraction")


# skrocenie ulamka, np. [2, 4] -> [1, 2]
def reduce_frac(frac):

    validate_frac(frac)
    return [frac[0]/gcd(frac[0], frac[1]), frac[1]/gcd(frac[0], frac[1])]


# frac1 + frac2
def add_frac(frac1, frac2):

    validate_frac(frac1)
    validate_frac(frac2)

    if frac1[1] == frac2[1]:
        return reduce_frac([frac1[0]+frac2[0], frac1[1]])

    frac1_temp = [frac1[0]*frac2[1], frac1[1]*frac2[1]]
    frac2_temp = [frac2[0]*frac1[1], frac2[1]*frac1[1]]

    return reduce_frac([frac1_temp[0]+frac2_temp[0], frac1_temp[1]])


# frac1 - frac2
def sub_frac(frac1, frac2):

    validate_frac(frac1)
    validate_frac(frac2)

    if frac1[1] == frac2[1]:
        return reduce_frac([frac1[0]-frac2[0], frac1[1]])

    frac1_temp = [frac1[0]*frac2[1], frac1[1]*frac2[1]]
    frac2_temp = [frac2[0]*frac1[1], frac2[1]*frac1[1]]

    return reduce_frac([frac1_temp[0]-frac2_temp[0], frac1_temp[1]])


# frac1 * frac2
def mul_frac(frac1, frac2):

    validate_frac(frac1)
    validate_frac(frac2)
    return reduce_frac([frac1[0]*frac2[0], frac1[1]*frac2[1]])


# frac1 / frac2
def div_frac(frac1, frac2):

    validate_frac(frac1)
    validate_frac(frac2)

    if frac2[0] == 0:
        raise ZeroDivisionError

    return reduce_frac([frac1[0]*frac2[1], frac1[1]*frac2[0]])


# bool, czy dodatni
def is_positive(frac):

    validate_frac(frac)
    return frac[0]*frac[1] > 0


# bool, typu [0, x]
def is_zero(frac):

    validate_frac(frac)
    return frac[0] == 0


# -1 | 0 | +1
def cmp_frac(frac1, frac2):

    validate_frac(frac1)
    validate_frac(frac2)

    if reduce_frac(frac1) == reduce_frac(frac2):
        return 0

    frac1_temp = reduce_frac([frac1[0]*frac2[1], frac1[1]*frac2[1]])
    frac2_temp = reduce_frac([frac2[0]*frac1[1], frac2[1]*frac1[1]])

    return 1 if frac1_temp[0] > frac2_temp[0] else -1


# konwersja do float
def frac2float(frac):

    validate_frac(frac)
    return float(frac[0])/frac[1]


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_reduce_frac(self):
        self.assertEqual(reduce_frac([2, 4]), [1, 2])
        self.assertRaises(Exception, reduce_frac, [2, 0])

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([2, 4], [3, 4]), [5, 4])
        self.assertRaises(Exception, add_frac, [1, 0], [1, 3])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([2, 3], [1, 2]), [1, 6])
        self.assertEqual(sub_frac([1, 2], [1, 2]), self.zero)
        self.assertRaises(Exception, sub_frac, [2, 0], [1, 2])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([2, 3], [3, 4]), [1, 2])
        self.assertEqual(mul_frac([6, 1], [3, 4]), [9, 2])
        self.assertRaises(Exception, mul_frac, [2, 3], [3, 0])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [3, 4]), [2, 3])
        self.assertEqual(div_frac([3, 2], [1, 2]), [3, 1])
        self.assertRaises(ZeroDivisionError, div_frac, [1, 2], self.zero)
        self.assertRaises(Exception, div_frac, [1, 2], [1, 0])
        self.assertRaises(Exception, div_frac, [1, 0], [1, 4])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertRaises(Exception, is_positive, [1, 0])

    def test_is_zero(self):
        self.assertTrue(is_zero(self.zero))
        self.assertTrue(is_zero([0, 12]))
        self.assertRaises(Exception, is_zero, [0, 0])

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([2, 3], [1, 2]), 1)
        self.assertEqual(cmp_frac([4, 17], [5, 18]), -1)
        self.assertEqual(cmp_frac([2, 4], [1, 2]), 0)
        self.assertRaises(Exception, cmp_frac, [2, 4], [1, 0])

    def test_frac2float(self):
        self.assertEqual(frac2float([3, 4]), 0.75)
        self.assertEqual(frac2float([4, 8]), 0.5)
        self.assertRaises(Exception, frac2float, [2, 0])

    def tearDown(self):
        del self.zero


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
