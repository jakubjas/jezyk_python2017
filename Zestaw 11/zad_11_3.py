import random


#rozne liczby od 0 do N-1 w kolejnosci losowej
def random_list(n):
    random_l = list(range(n))
    random.shuffle(random_l)
    return random_l


# Wersja wg Kernighana i Ritchiego.
def shellsort(L, left, right, cmpfunc=cmp):
    h = (right - left) / 2
    while h > 0:
        for i in range(left + h, right + 1):
            for j in range(i, left + h - 1, -h):
                if cmpfunc(L[j-h], L[j]) > 0:
                    L[j-h], L[j] = L[j], L[j-h]
        h /= 2


N = 10
mylist = random_list(N)
list_reverse = list(mylist)

# Zwykle sortowanie.
shellsort(mylist, 0, N-1)

print str(mylist)

# Sortowanie w odwrotnej kolejnosci.
shellsort(list_reverse, 0, N-1, cmpfunc=lambda x, y: -cmp(x, y))

print str(list_reverse)
