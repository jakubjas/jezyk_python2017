def vertical_line(number):
    result = "|"
    for i in range(number):
        result += "   |"
    return result


def horizontal_line(number):
    result = "+"
    for i in range(number):
        result += "---+"
    return result


reply = raw_input("\nPodaj ilosc kratek w pionie: ")

try:
    vertical_squares = int(reply)

except ValueError:

    print "To nie jest liczba!"
    exit()

reply = raw_input("Podaj ilosc kratek w poziomie: ")

try:
    horizontal_squares = int(reply)

except ValueError:

    print "To nie jest liczba!"
    exit()

squares = "\n" + horizontal_line(horizontal_squares) + "\n"

for i in range(vertical_squares):
    squares += vertical_line(horizontal_squares) + "\n" + horizontal_line(horizontal_squares) + "\n"

print squares
