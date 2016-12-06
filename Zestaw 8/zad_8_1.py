def solve1(a, b, c):
    if a == 0 and b == 0:
        if c == 0:
            print "Rownanie nieokreslone, warunki spelnia dowolna para (x, y), gdzie x e R i y e R"
            return
        else:
            print "Rownanie sprzeczne, brak rozwiazan"
            return
    if a == 0:
        print "Zbior rozwiazan okresla prosta y = " + str(float(-c)/float(b)) + ", x e R"
        return
    if b == 0:
        print "Zbior rozwiazan okresla prosta x = " + str(float(-c)/float(a)) + ", y e R"
        return

    result = str(float(-a)/float(b)) + " * x + " + str(float(-c)/float(b)) + ", x e R"

    print "Zbior rozwiazan okresla prosta y = " + result


solve1(2, 1, -1)
solve1(63, -7, 14)
solve1(0, 0.5, -11)
solve1(0.5, 0, -11)
