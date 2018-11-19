class Przedmiot:

    def __init__(self, nazwa, bonus_do_ataku):
        self.nazwa = nazwa
        self.bonus_do_naparzania = bonus_do_naparzania

    def __str__(self):
        return f('{self.nazwa}, {self.bonus_do_naparzania} do ataku')
