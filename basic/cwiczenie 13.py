suma_temperatur = 0
i = 0
while True:
    dane = input("podaj temperaturę lub wpisz k by zakończyć")
    if dane == "k":
        break
    suma_temperatur += float(dane)
    i +=1
print("srednia temerattura to: ", round(suma_temperatur/1,2))