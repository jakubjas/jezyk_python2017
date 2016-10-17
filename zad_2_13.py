def words_length(line):
    return sum([len(word) for word in line.split()])

line = """tatarak
heban

elokwentny

cytryna

uzurpowac
rekonwalescencja
energia"""

print words_length(line)