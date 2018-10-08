liczba = input("podaj liczbę: ")
liczba = int(liczba)

print(f"większa od 10: {liczba>10}")
print(f"mniejsza od 15: {liczba<=15}")
print(f"podzielna przez 2: {liczba%2==0}")

print(f"większa od 10 lub podzielna przez 5: {liczba>10 or liczba%5==0}")