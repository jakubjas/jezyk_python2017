# wersja rekurencyjna
def list_reverse_recursive(source_list, left, right):

    if left >= right:
        return None

    source_list[left], source_list[right] = source_list[right], source_list[left]
    list_reverse_recursive(source_list, left+1, right-1)


# wersja iteracyjna
def list_reverse_iterative(source_list, left, right):
    for i in range((right-left)/2):
        source_list[left+i], source_list[right-i] = source_list[right-i], source_list[left+i]

list1 = [1, 4, 6, 8, 10, 12, 13]
list2 = [1, 2, 3, 4, 5, 6]

print list1

list_reverse_iterative(list1, 0, 2)

print list1

print list2

list_reverse_recursive(list2, 1, 4)

print list2
