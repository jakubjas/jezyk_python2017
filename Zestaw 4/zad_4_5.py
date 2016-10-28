# wersja rekurencyjna
def list_reverse_recursive(l, left, right):

    if left >= right:
        return None

    l[left], l[right] = l[right], l[left]
    list_reverse_recursive(l, left+1, right-1)


# wersja iteracyjna
def list_reverse_iterative(l, left, right):
    for i in range((right-left)/2):
        l[left+i], l[right-i] = l[right-i], l[left+i]

l1 = [1, 4, 6, 8, 10, 12, 13]
l2 = [1, 2, 3, 4, 5, 6]

print l1

list_reverse_iterative(l1, 0, 2)

print l1

print l2

list_reverse_recursive(l2, 1, 4)

print l2
