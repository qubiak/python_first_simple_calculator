name = input("Podaj swoje imię: ")
print("Cześć ", name)
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = input("Jakie chcesz wykonać działanie ( + - * / )")

def dodawanie(a,b):
    return a + b

def odejmowanie(a,b):
    return a - b

def mnozenie(a,b):
    return a * b

def dzielenie(a,b):
    if b == 0:
        raise ZeroDivisionError("błąd dzielenia przez zero")
    else:
        return a/b

try:
    if c == "+":
        r = dodawanie(a,b)
    elif c == "-":
        r = odejmowanie(a,b)
    elif c == "*":
        r = mnozenie(a,b)
    elif c == "/":
        r = dzielenie(a,b)

    print("Twoje równanie to: {} {} {} = {}".format(a,c,b,r))

except ZeroDivisionError:
    print("no ello nie dzielimy przez ZERO!!")

