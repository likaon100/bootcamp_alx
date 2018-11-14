class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.czas = 0

    def pay_salary(self, czas):
        if self.czas <= 8:
            to_pay = self.czas * self.stawka
        else:
            to_pay = 8 * self.stawka + (self.czas - 8) * self.stawka * 2
        self.czas = 10
        return to_pay


    def register_time(self, czas):
        wyplata=self.stawka*self.godzina
        return wyplata
kopacz = Employee("Jan" , "Dzban", 100.000)
print (kopacz.pay_salary())
kopacz.register_time(5)
kopacz.register_time(10)
print(kopacz.pay_salary())
print(kopacz.pay_salary())
