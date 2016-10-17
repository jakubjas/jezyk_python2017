def first_letters(line):
    return "".join([word[0] for word in line.split()])

def last_letters(line):
    return "".join([word[len(word) - 1] for word in line.split()])

line = """tatarak
heban

elokwentny

cytryna

uzurpowac
rekonwalescencja
energia"""

line2 = """audiofil
skladowy
butelkowiec
pastylki
melancholia
"""

print first_letters(line)
print last_letters(line2)

#test komentarza