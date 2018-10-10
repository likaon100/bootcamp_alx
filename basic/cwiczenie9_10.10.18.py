# przyjecie argumentow

a = int(input("podaj liczbe pierwsza"))
b = int(input("podaj liczbe druga"))
operacja = input("Jaka operacja? [+-*/]")

# ify na operacje

    a = int(a)
    b = int(b)
    if operacja == "+":
        wynik = a + b
    elif operacja == "-":
        wynik = a - b
    elif operacja == "*":
        wynik = a * b
    elif operacja == "/":
        if b == 0:
            wynik = "nie dziel przez zero!"
        else:
            wynik = a / b
    else:
        print("niezrozumiala operacja")
print(f"wynik dzialania {operacja}: {a}, {b} to: {wynik}")
