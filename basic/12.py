#sortowanie przez wybieranie
#asert sprawdzenie - test
#indeks (0,1,2,3,4)
lista = [2,3,5,4,1]

print ("Liczby przed:", lista)

for indeks_podstawienie in range (len(lista)):
    indeks_min_wartosc = indeks_podstawienie
    for indeks_ogona in range (indeks_podstawienie+1, len(lista)):
        if lista[indeks_ogona]<lista[indeks_min_wartosc]:
            indeks_min_wartosc=indeks_ogona
    value_temp =lista[indeks_min_wartosc]
    lista[indeks_min_wartosc]=lista[indeks_podstawienie]
    lista[indeks_podstawienie]=value_temp

print("liczy po: ", lista)


