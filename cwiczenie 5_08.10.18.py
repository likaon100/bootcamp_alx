
Miasto_A = input("Miasto_A: ")
Miasto_B = input("Miasto_B: ")
odległość = int(input("odległość {Miasto_A}={Miasto_B}: "))
cena_paliwa= float(input("cena_paliwa: "))
spalanie = float(input("spalanie: "))
print()

koszty = ((odległość/100) * spalanie * cena_paliwa)
koszty = round(koszty,3)

print (f"koszty {Miasto_A}-{Miasto_B} to {koszty} PLN")