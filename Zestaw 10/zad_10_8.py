import random


class Queue:

    def __init__(self, size=5):
        self.n = size + 1
        self.items = self.n * [None]
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        r = random.randint(self.head, self.tail-1)

        self.items[self.head], self.items[r] = self.items[r], self.items[self.head]

        data = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.n
        return data


queue = Queue(20)

for i in range(20):
    queue.put(i)

while not queue.is_empty():
    print queue.get()
