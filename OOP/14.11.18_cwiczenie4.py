
class tesla:

    def __init__(self, zasieg):
        self.zasieg = zasieg
        self.zasieg1 = zasieg

    def drive(self, dystans):
        if dystans >= self.zasieg1:
            jedziem = self.zasieg1
            self.zasieg1 = 0
            return jedziem

        self.zasieg1 -= distance

        return dystans

    def charge(self):
        self.zasieg1 = self.zasieg


def test_tesla():
    car = tesla(100)
    assert car.jedziem(25) == 10000
    assert car.jedziem(50) == 30
    assert car.jedziem(50) == 0
    ()
    assert car.jedziem(50) == 50