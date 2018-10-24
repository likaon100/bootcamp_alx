liczby = set()

while True:
    a = input("Wprowadź liczbę albo napisz że 'koniec' aby to  zakończyć: ")
    if a == 'koniec':
        break
    liczba = int(a)
    liczby.add(liczba)
print()
print(len(liczby & set(range(1,101))))
print()

print("( ͡° ͜ʖ ͡°)╭∩╮")