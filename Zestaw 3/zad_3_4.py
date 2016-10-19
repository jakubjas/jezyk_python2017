while True:
    reply = raw_input("Podaj liczbe rzeczywista: ")
    if reply == "stop":
        break
    try:
        number = float(reply)
    except ValueError:
        print "To nie jest liczba!"
    else:
        print pow(number, 3)
