from random import randint

from przedmiot import Przedmiot


class Postac():
    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self.atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.ekwipunek = []



    def przedstaw_sie(self):
        # print(f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia")
        print(self)

    def __str__(self):
        return f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia"

    def otrzymaj_obrazenia(self, ile):
        print(f"{self.imie} oberwal za {ile} obrazen")
        self.zdrowie = self.zdrowie - ile
        if self.zdrowie < 0:
            self.zdrowie = 0

    def czy_zyje(self):
        return self.zdrowie > 0

    def moc_ataku(self):
        wynik = randint(self.atak // 2, self.atak)
        return wynik

    # losowe - random import randint(od jakiej wartości do jakiej)

    @staticmethod
    def walka(atakujacy, broniacy):
        print(f"Walka: {atakujacy.imie} vs {broniacy.imie}")
        print(atakujacy)
        print(broniacy)
        broniacy.otrzymaj_obrazenia(atakujacy.atak)
        print(f'atakujacy uderza {broniacy.imie} za {atakujacy.atak} obrażeń')
        atakujacy.otrzymaj_obrazenia(broniacy.atak)

    def wylecz(self):
        return self.zdrowie > 0

    def leczenie(self, lek):
        if self.zdrowie + lek < self.max_zdrowie:
            self.zdrowie = self.zdrowie + lek
        else:
            self.zdrowie = self.max_zdrowie


rufus = Postac("Rufus", 13, 3000)
agata = Postac("agata", 34, 2500)

tulipan = Przedmiot('wombat', 5)



Postac.walka(rufus, agata)
rufus.przedstaw_sie()
rufus.otrzymaj_obrazenia(10)
rufus.max_zdrowie = 200
agata.max_zdrowie = 2555
print(rufus)
rufus.otrzymaj_obrazenia(5)
rufus.leczenie(0)
print(rufus)
print(agata)

# def test_nowa_postac():
#     postac = Postac("Albert",1,20)
#     assert postac.imie
#
print("( ͡° ͜ʖ ͡°)╭∩╮")
