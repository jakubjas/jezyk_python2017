class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if self.data < data:      # na prawo
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        elif self.data > data:    # na lewo
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            pass

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return False


def bst_max(top):
    if top is None:
        raise ValueError("Empty tree")
    if top.right is None:
        return top.data
    else:
        return bst_max(top.right)


def bst_min(top):
    if top is None:
        raise ValueError("Empty tree")
    if top.left is None:
        return top.data
    else:
        return bst_min(top.left)


root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(7)
root.insert(8)
root.insert(1020)
root.insert(0)

print "Max: " + str(bst_max(root))
print "Min: " + str(bst_min(root))
