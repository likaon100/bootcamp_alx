napis = input("Podaj napis: ")
ile_liter = {}
for litera in napis:
    if litera != " ":
        ile_liter[litera] = ile_liter.get(litera, 0) + 1
for litera in ile_liter:

    print (f"|| litera: {litera} jest w wyrazie {ile_liter[litera]} razy ||")

print()
print()

print("( ͡° ͜ʖ ͡°)╭∩╮")
print()
print()
print("=_="*20)