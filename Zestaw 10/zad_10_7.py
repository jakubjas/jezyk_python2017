import random


class PriorityQueue:

    def __init__(self, cmpfunc=cmp):
        self.items = []
        self.cmpfunc = cmpfunc

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.cmpfunc(self.items[i], self.items[maxi]) > 0:
                maxi = i
        return self.items.pop(maxi)


def cmpfunc1(x, y):
    return cmp(x, y)


def cmpfunc2(x, y):
    return cmp(y, x)


print "Posortowane malejaco: "

# w kolejnosci od najwiekszej wartosci do najmniejszej
queue1 = PriorityQueue(cmpfunc1)

for i in range(10):
    queue1.insert(random.randint(0, 30))

while not queue1.is_empty():
    print queue1.remove()

print "Posortowane rosnaca: "

# w kolejnosci od najmniejszej wartosci do najwiekszej
queue1 = PriorityQueue(cmpfunc2)

for j in range(10):
    queue1.insert(random.randint(0, 30))

while not queue1.is_empty():
    print queue1.remove()
