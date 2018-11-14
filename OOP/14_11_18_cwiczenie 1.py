class Osoba:
    imie = "Jan"
    nazwisko = "Kowalski"

    def przedstaw_sie(self):
        print("YOLO Nazywam się (self.imie) (self.nazwisko)")

obiekt = Osoba()
obiekt2 = Osoba()
obiekt2.imie="Karol"

print.przedstaw_sie()
print2.przedstaw_sie()

obiekt.metoda_statyczna()