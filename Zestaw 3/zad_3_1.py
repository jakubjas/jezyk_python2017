# kody poprawione, zgodne z konwencja PEP 8

# kod 1
x = 2
y = 3

if x > y:
    result = x
else:
    result = y

# kod 2

for i in "qwerty":
    if ord(i) < 100:
        print i

# kod 3

for i in "axby":
    print ord(i) if ord(i) < 100 else i

    #