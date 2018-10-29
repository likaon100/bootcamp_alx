
def czy_pierwsza(liczba):
    for dziel in range(2, liczba):
        if liczba % dziel == 0:
            return False
    return True

def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_pierwsza(7)
    assert czy_pierwsza(17)
    assert czy_pierwsza(23)

def test_czy_jest_pierwsza_dla_liczby_nie_pierwszej():
    assert not czy_pierwsza(4)
    assert not czy_pierwsza(9)
    assert not czy_pierwsza(12)


#asercja = sprowadzenie wartości po prawej stronie do wartosci logicznej

