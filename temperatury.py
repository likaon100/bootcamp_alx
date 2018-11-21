class Temperatura:
    def __init__(self, x):
        self._wartosc = x

    def __str__(self):
        return f"temperatura: {self.wartosc} stopni celcjusza"

    @property
    def wartosc(self):
        print('getter')
        return self._wartosc

    @wartosc.setter
    def wartosc(self, x):
        print('setter')
        if x < -273:
            raise ValueError('Temperatura za niska')
        self._wartosc = x


x = Temperatura(20)
x.wartosc = -300
print(x)
print(x.wartosc)
x.wartosc = -300
