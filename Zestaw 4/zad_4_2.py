# funkcja skonstruowana z kodu z zadania 3.5
def draw_ruler(num):
    try:
        length = int(num)

    except ValueError:

        print "To nie jest liczba!"
        exit()

    ruler = "|"

    for i in range(1, length + 1):
        ruler += "....|"

    ruler += "\n0"

    for i in range(1, length + 1):

        # obliczam pozostale miejsce, aby moc wyrownac liczbe do pionowej kreski
        space = 5 - len(str(i))

        for j in range(space):
            ruler += " "

        ruler += str(i)

    return ruler


# funkcja skonstruowana z kodu z zadania 3.6
def draw_squares(height, width):

    def vertical_line(number):
        result = "|"
        for j in range(number):
            result += "   |"
        return result

    def horizontal_line(number):
        result = "+"
        for k in range(number):
            result += "---+"
        return result

    try:
        vertical_squares = int(height)

    except ValueError:

        print "Podana wysokosc nie jest liczba!"
        exit()

    try:
        horizontal_squares = int(width)

    except ValueError:

        print "Podana szerokosc nie jest liczba!"
        exit()

    squares = "\n" + horizontal_line(horizontal_squares) + "\n"

    for i in range(vertical_squares):
        squares += vertical_line(horizontal_squares) + "\n" + horizontal_line(horizontal_squares) + "\n"

    return squares


print draw_ruler(12)
print draw_squares(2, 4)
