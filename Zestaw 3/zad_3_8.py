def list_intersection(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    return list(s1.intersection(s2))


def list_no_duplicates(l1, l2):
    l = l1 + l2
    return list(set(l))

L1 = [1, 2, 3, 4, 5]
L2 = [2, 3, 4, 5, 6]

print "\nSekwencja 1: "
print L1
print "\nSekwencja 2: "
print L2
print "\nLista elementow wystepujacych w obu sekwencjach (bez powtorzen):"
print list_intersection(L1, L2)
print "\nLista wszystkich elementow z obu sekwencji (bez powtorzen)"
print list_no_duplicates(L1, L2)
