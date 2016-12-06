import math


def heron(a, b, c):
    if a+b <= c or a+c <= b or b+c <= a:
        raise ValueError("Podane liczby nie spelniaja warunku trojkata")
    p = 0.5 * (a + b + c)
    return math.sqrt(p * (p-a) * (p-b) * (p-c))


print heron(3, 4, math.sqrt(9+16))
print heron(16, 16, 16)
