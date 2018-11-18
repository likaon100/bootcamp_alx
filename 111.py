produkty = {
    "ziemniaki": 3,
    "cebula": 2,
    "woda": 1.5,
    "piwo": 2.5,
    "zimioki": 3.5,
    "browarek": 4.0,
}

koszyk = {}

while True:
    print("W naszym sklepie oferujemy: ")
    for produkt in produkty:
        print(f" - {produkt} - w cenie: {produkty[produkt]} PLN")

    print()
    wybor_produktu = input("Który produkt chcesz kupić? (wpisz koniec aby zakończyć ")
    if wybor_produktu == "koniec":
        break
    if wybor_produktu in produkty:
        ile = input(f"Ile chcesz kupić [{wybor_produktu}]")
        cena = int(ile) * produkty[wybor_produktu]
        koszyk[wybor_produktu] = cena
    else:
        print(f"Zapłacisz: {cena}")

for produkt in koszyk:
    print (f" - {produkt}: {koszyk[produkt]}")

    print(":):):):):)")

print ("Twój rachunek")
sumarycznie = 0
for "produkty"