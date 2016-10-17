def sort_num_and_stringify(L):
    L.sort()
    return "".join(map(str, L))

L = [1,4,5,8,13,10]

print sort_num_and_stringify(L)