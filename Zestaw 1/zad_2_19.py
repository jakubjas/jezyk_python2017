def fill_with_zeroes(L):
    return " ".join(number.zfill(3) for number in map(str, L))

L = [1, 2, 43, 123, 9, 4, 88, 97, 145]

print fill_with_zeroes(L)