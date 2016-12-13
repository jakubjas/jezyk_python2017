class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def insert_head(node, data):   # algorytm klasy O(1)
    return Node(data, node)


def insert_tail(node, data):   # algorytm klasy O(N)
    head = node
    last = None
    while node:
        last = node
        node = node.next
    if last is None:      # lista byla pusta
        return Node(data)
    else:                 # last jest ostatni
        last.next = Node(data)
        return head   # head sie nie zmienil


def print_forward(node):
    if node:
        print node
        print_forward(node.next)


def get_last_node(node):
    if node is not None:
        while node.next:
            node = node.next
    return node


def merge(node1, node2):
    last1 = get_last_node(node1)
    if last1 is not None:
        last1.next = node2
        return node1
    else:
        return node2


head1 = None
head1 = insert_head(head1, 1)
head1 = insert_tail(head1, 2)
head1 = insert_tail(head1, 3)

print "Pierwsza lista: "
print_forward(head1)

head2 = None
head2 = insert_head(head2, 4)
head2 = insert_tail(head2, 5)
head2 = insert_tail(head2, 6)

print "Druga lista: "
print_forward(head2)

head3 = merge(head1, head2)

del head1
del head2

print "Po zlaczeniu: "
print_forward(head3)
