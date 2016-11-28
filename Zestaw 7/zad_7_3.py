import unittest
from points import Point
from math import pi


class Circle:

    def __init__(self, x=0.0, y=0.0, radius=1.0):
        if not self.isnumber(x) or not self.isnumber(y) or not self.isnumber(radius):
            raise ValueError("Niepoprawne dane")
        elif radius < 0:
            raise ValueError("Promien ujemny")

        self.pt = Point(x, y)
        self.radius = radius

    def isnumber(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def __repr__(self):            # "Circle(x, y, radius)"
        return "Circle(%s, %s, %s)" % (self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Proba porownania obiektow roznych typow")
        return self.pt == other.pt and abs(self.radius - other.radius) <= 0.0000000001

    def __ne__(self, other):
        return not self == other

    def area(self):                # pole powierzchni
        return pi*self.radius*self.radius

    def move(self, x, y):          # przesuniecie o (x, y)
        if not self.isnumber(x) or not self.isnumber(y):
            raise ValueError("Niepoprawne dane")
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):        # okrag pokrywajacy oba
        if not isinstance(other, Circle):
            raise ValueError("Niepoprawne dane")

        if self.radius > other.radius:
            first_circle = other
            second_circle = self
        else:
            first_circle = self
            second_circle = other

        distance = (first_circle.pt - second_circle.pt).length()

        # jesli jeden okrag zawarty jest w drugim - zwroc wiekszy
        if (distance + first_circle.radius) <= second_circle.radius:
            return Circle(second_circle.pt.x, second_circle.pt.y, second_circle.radius)
        else: # w przeciwnym razie wyznacz okrag pokrywajacy
            theta = 0.5 + (second_circle.radius-first_circle.radius) / (2*distance)
            p1 = Point((1-theta)*first_circle.pt.x, (1-theta)*first_circle.pt.y)
            p2 = Point(theta*second_circle.pt.x, theta*second_circle.pt.y)
            center = p1 + p2
            radius = (distance + first_circle.radius + second_circle.radius)/2
            return Circle(center.x, center.y, radius)


# Kod testujacy modul.

class TestCircle(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(ValueError):
            Circle("fd", 3, 1)
        with self.assertRaises(ValueError):
            Circle(1, 3, -2)

    def test_repr(self):
        self.assertEqual(Circle(1, 2, 3).__repr__(), "Circle(1, 2, 3)")

    def test_eq(self):
        self.assertTrue(Circle(1, 2, 3) == Circle(1, 2, 3))
        self.assertFalse(Circle(3, 3, 3) == Circle(1, 2, 3))
        self.assertRaises(ValueError, Circle.__eq__, Circle(1, 2, 3), "f")

    def test_ne(self):
        self.assertTrue(Circle(1, 3, 3) != Circle(1, 2, 3))
        self.assertFalse(Circle(1, 2, 3) != Circle(1, 2, 3))

    def test_area(self):
        self.assertEqual(Circle(1, 1, 1).area(), pi)
        self.assertEqual(Circle(1, 2, 3).area(), pi*9)

    def test_move(self):
        self.assertEqual(Circle(1, 1, 3).move(0, 1), Circle(1, 2, 3))
        self.assertEqual(Circle(0, 1, 3).move(1, 1), Circle(1, 2, 3))
        self.assertRaises(ValueError, Circle(1, 2, 3).move, "f", 1)

    def test_cover(self):
        self.assertEqual(Circle(0, 2, 6).cover(Circle(-5, 2, 2)), Circle(-0.5, 2.0, 6.5))
        self.assertEqual(Circle(1, 3, 1).cover(Circle(-6, 3, 2)), Circle(-3.0, 3.0, 5.0))
        self.assertEqual(Circle(3, 1, 8).cover(Circle(3, 0, 8)), Circle(3.0, 0.5, 8.5))
        self.assertEqual(Circle(4, 6, 10).cover(Circle(4, 1, 5)), Circle(4.0, 6.0, 10.0))
        self.assertRaises(ValueError, Circle(1, 2, 3).cover, "f")


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy