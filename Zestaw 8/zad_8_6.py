import time


# wersja rekurencyjna
def P(i, j):
    if i < 0 or j < 0:
        raise ValueError("Bledne dane")
    if i == 0 and j == 0:
        return 0.5
    if i > 0 and j == 0:
        return 0.0
    if i == 0 and j > 0:
        return 1.0
    else:
        return 0.5 * (P(i-1, j) + P(i, j-1))


P_dict = {(0, 0): 0.5}  # globalny slownik


# wersja dynamiczna
def P_dynamic(i, j):
    if i < 0 or j < 0:
        raise ValueError("Bledne dane")
    if i > 0 and j == 0:
        return 0.0
    if i == 0 and j > 0:
        return 1.0
    else:
        if P_dict.get((i, j)) is not None:
            return P_dict[(i, j)]
        else:
            P_dict[(i, j)] = 0.5 * (P_dynamic(i-1, j) + P_dynamic(i, j-1))
            return P_dict[(i, j)]


def compare_exec_time(i, j):
    start = time.clock()
    P_value = P(i, j)
    P_exec_time = time.clock() - start
    start = time.clock()
    P_dynamic_value = P_dynamic(i, j)
    P_dynamic_exec_time = time.clock() - start

    print "Wartosc zwrocona przez P(" + str(i) + ", " + str(j) + ") = " + str(P_value) + " Czas wykonania: " + str(P_exec_time)
    print "Wartosc zwrocona przez P_dynamic(" + str(i) + ", " + str(j) + ") = " + str(P_dynamic_value) + " Czas wykonania: " + str(P_dynamic_exec_time)

compare_exec_time(20, 5)
compare_exec_time(15, 12)
