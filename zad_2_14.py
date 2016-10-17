def longest_word(line):
    return max(line.split(),key=len)

line = """tatarak
heban

elokwentny

cytryna

uzurpowac
rekonwalescencja
energia"""

print longest_word(line)

#test