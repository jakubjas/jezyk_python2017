class Stack:

    def __init__(self, size=10):
        self.items = size * [None]
        self.already_present = size * [0]
        self.n = 0
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.already_present[data] == 1:
            return
        self.items[self.n] = data
        self.already_present[data] = 1
        self.n += 1

    def pop(self):
        self.n -= 1
        data = self.items[self.n]
        self.already_present[data] = 0
        self.items[self.n] = None
        return data

    def print_all(self):
        while not self.is_empty():
            print(self.pop())


stack = Stack()
stack.push(1)
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.pop()
stack.push(2)
stack.push(3)
stack.print_all()
