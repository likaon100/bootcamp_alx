class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.czas = 0

    def pay_salary(self):
        if self.czas <= 8:
            to_pay = self.czas * self.stawka
        else:
            to_pay = 8 * self.stawka + (self.czas - 8) * self.stawka * 2
        self.czas = 0
        return to_pay