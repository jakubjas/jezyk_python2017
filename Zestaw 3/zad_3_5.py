reply = raw_input("Podaj dlugosc miarki: ")

try:
    length = int(reply)

except ValueError:

    print "To nie jest liczba!"
    exit()

ruler = "|"

for i in range(1, length+1):
    ruler += "....|"

ruler += "\n0"

for i in range(1, length+1):

    # obliczam pozostale miejsce, aby moc wyrownac liczbe do pionowej kreski
    space = 5 - len(str(i))

    for j in range(space):
        ruler += " "

    ruler += str(i)

print ruler
