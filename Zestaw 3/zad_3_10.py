# metoda 1
D1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# metoda 2
D2 = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])

# metoda 3
D3 = dict(zip(['I', 'V', 'X', 'L', 'C', 'D', 'M'], [1, 5, 10, 50, 100, 500, 1000]))

# metoda 4
D4 = dict()
D4['I'] = 1
D4['V'] = 5
D4['X'] = 10
D4['L'] = 50
D4['C'] = 100
D4['D'] = 500
D4['M'] = 1000


def roman2int(roman):

    d = dict(zip(['I', 'V', 'X', 'L', 'C', 'D', 'M'], [1, 5, 10, 50, 100, 500, 1000]))

    roman = roman.upper().strip()
    integer = 0

    try:
        for i in range(len(roman)):
            value = d[roman[i]]

            if i+1 < len(roman) and d[roman[i+1]] > value:
                integer -= value
            else:
                integer += value

    except KeyError:

        print "To nie jest poprawna liczba w zapisie rzymskim!"
        exit()

    return integer


print roman2int('MMMCCCXXXVIII')