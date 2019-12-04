from kreis import kreis
from numpy import pi

def test_kreis():
    r = 1
    k = kreis(r)
    assert k.umfang() == 2 * pi
    assert k.flaeche() == pi

    r = 0
    k = kreis(r)
    assert k.umfang() == 0
    assert k.flaeche() == 0
