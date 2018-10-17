lista =[]

while len(lista)<10:
    x=input("Podaj liczbę lub 'k' żeby zakończyć:")
    if x=="k":
        break
    liczba=int(x)
    lista.append(liczba)
srednia=sum(lista)/len(lista)

print(f"średnia to {srednia}")
