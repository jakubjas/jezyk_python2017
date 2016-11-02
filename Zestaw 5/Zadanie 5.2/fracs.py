#!/usr/bin/python

import unittest
from fractions import gcd


# skrocenie ulamka, np. [2, 4] -> [1, 2]
def reduce_frac(frac):

    if frac[1] == 0:
        return None
    else:
        return [frac[0]/gcd(frac[0], frac[1]), frac[1]/gcd(frac[0], frac[1])]


# frac1 + frac2
def add_frac(frac1, frac2):

    if frac1[1] == 0 or frac2[1] == 0:
        return None

    elif frac1[1] != frac2[1]:
        frac1_temp = [frac1[0]*frac2[1], frac1[1]*frac2[1]]
        frac2_temp = [frac2[0]*frac1[1], frac2[1]*frac1[1]]

        return reduce_frac([frac1_temp[0]+frac2_temp[0], frac1_temp[1]])

    else:
        return reduce_frac([frac1[0]+frac2[0], frac1[1]])


# frac1 - frac2
def sub_frac(frac1, frac2):

    if frac1[1] == 0 or frac2[1] == 0:
        return None

    elif frac1[1] != frac2[1]:
        frac1_temp = [frac1[0]*frac2[1], frac1[1]*frac2[1]]
        frac2_temp = [frac2[0]*frac1[1], frac2[1]*frac1[1]]

        return reduce_frac([frac1_temp[0]-frac2_temp[0], frac1_temp[1]])

    else:
        return reduce_frac([frac1[0]-frac2[0], frac1[1]])


# frac1 * frac2
def mul_frac(frac1, frac2):

    if frac1[1] == 0 or frac2[1] == 0:
        return None
    else:
        return reduce_frac([frac1[0]*frac2[0], frac1[1]*frac2[1]])


# frac1 / frac2
def div_frac(frac1, frac2):

    if frac1[1] == 0 or frac2[0] == 0 or frac2[1] == 0:
        return None
    else:
        return reduce_frac([frac1[0] * frac2[1], frac1[1] * frac2[0]])


# bool, czy dodatni
def is_positive(frac):

    if frac[1] == 0:
        return None
    else:
        return frac[0]*frac[1] > 0


# bool, typu [0, x]
def is_zero(frac):

    if frac[1] == 0:
        return None
    else:
        return frac[0] == 0


# -1 | 0 | +1
def cmp_frac(frac1, frac2):

    if frac1[1] == 0 or frac2[1] == 0:
        return None

    elif reduce_frac(frac1) != reduce_frac(frac2):
        frac1_temp = reduce_frac([frac1[0] * frac2[1], frac1[1] * frac2[1]])
        frac2_temp = reduce_frac([frac2[0] * frac1[1], frac2[1] * frac1[1]])

        return 1 if frac1_temp[0]>frac2_temp[0] else -1

    else:
        return 0


# konwersja do float
def frac2float(frac):

    if frac[1] == 0:
        return None
    else:
        return float(frac[0])/frac[1]


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_reduce_frac(self):
        self.assertEqual(reduce_frac([2, 4]), [1, 2])
        self.assertEqual(reduce_frac([2, 0]), None)

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([2, 4], [3, 4]), [5, 4])
        self.assertEqual(add_frac([1, 0], [1, 3]), None)

    def test_sub_frac(self):
        self.assertEqual(sub_frac([2, 3], [1, 2]), [1, 6])
        self.assertEqual(sub_frac([1, 2], [1, 2]), self.zero)
        self.assertEqual(sub_frac([2, 0], [1, 2]), None)

    def test_mul_frac(self):
        self.assertEqual(mul_frac([2, 3], [3, 4]), [1, 2])
        self.assertEqual(mul_frac([6, 1], [3, 4]), [9, 2])
        self.assertEqual(mul_frac([2, 3], [3, 0]), None)

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [3, 4]), [2, 3])
        self.assertEqual(div_frac([3, 2], [1, 2]), [3, 1])
        self.assertEqual(div_frac([1, 2], [0, 4]), None)
        self.assertEqual(div_frac([1, 2], [1, 0]), None)
        self.assertEqual(div_frac([1, 0], [1, 4]), None)

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertEqual(is_positive([1, 0]), None)

    def test_is_zero(self):
        self.assertTrue(is_zero(self.zero))
        self.assertTrue(is_zero([0, 12]))
        self.assertEqual(is_zero([0, 0]), None)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([2, 3], [1, 2]), 1)
        self.assertEqual(cmp_frac([4, 17], [5, 18]), -1)
        self.assertEqual(cmp_frac([2, 4], [1, 2]), 0)
        self.assertEqual(cmp_frac([2, 4], [1, 0]), None)

    def test_frac2float(self):
        self.assertEqual(frac2float([3, 4]), 0.75)
        self.assertEqual(frac2float([4, 8]), 0.5)
        self.assertEqual(frac2float([2, 0]), None)

    def tearDown(self):
        del self.zero

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
