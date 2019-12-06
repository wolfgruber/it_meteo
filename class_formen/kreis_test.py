from kreis import kreis
from numpy import pi

def test_kreis():
    """Funktion zum Testen der Kreis-Klasse"""
    r = 1
    k = kreis(r)
    assert k.umfang() == 2 * pi
    assert k.flaeche() == pi

    r = 1/pi
    k = kreis(r)
    assert k.umfang() == 2
    assert k.flaeche() == r

    r = 0
    k = kreis(r)
    assert k.umfang() == 0
    assert k.flaeche() == 0
