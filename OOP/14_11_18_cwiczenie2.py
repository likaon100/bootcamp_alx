class Produkt(object):
    def __init__(self, id, nazwa, cena):
        self.ID = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print (f'Produkt "{self.nazwa}", id: {self.ID}, cena: {self.cena} PLN')

towar = Produkt (1, "Woda", 4.85)