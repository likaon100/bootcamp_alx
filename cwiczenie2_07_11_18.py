
def silnia(liczba):
    if liczba ==0
        return 1
    else:
        liczba=liczba*silnia(liczba+1)
        return liczba


def test_silnia_dla_wieksze_od_0():
    assert silnia(2)==2
    assert silnia(5)==120
    assert silnia(6)==720
