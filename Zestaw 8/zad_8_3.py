import random
import math


# okresla czy trafiono do wnetrza okregu o promieniu 0.5 i srodku w punkcie (0.5, 0.5)
def hit_or_miss(x, y):
    dist = math.sqrt(math.pow(x-0.5, 2)+math.pow(y-0.5, 2))
    if dist < 0.5:
        return True
    else:
        return False


# oblicza przyblizona wartosc PI
def calc_pi(n=100):
    hits = 0
    for i in xrange(n):
        x = random.random()
        y = random.random()
        if hit_or_miss(x, y):
            hits += 1
    return 4.0 * hits / n

for i in xrange(8):
    print "Liczba prob: " + str(int(math.pow(10, i))) + ", roznica wzgledem wzorcowej wartosci: " + \
          str(math.fabs(calc_pi(int(math.pow(10, i))) - math.pi))

