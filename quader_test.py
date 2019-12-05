from quader import quader

def test_quader():
    """Funktion zum Testen der quader-Klasse"""
    l = 1
    b = 1
    h = 1
    q = quader(l, b, h)
    assert q.flaeche() == 1
    assert q.umfang() == 4
    assert q.volumen() == 1

    l = 0
    b = 1
    h = 1
    q = quader(l, b, h)
    assert q.flaeche() == 0
    assert q.umfang() == 2
    assert q.volumen() == 0

    l = 1
    b = 0
    h = 1
    q = quader(l, b, h)
    assert q.flaeche() == 0
    assert q.umfang() == 2
    assert q.volumen() == 0

    l = 1
    b = 1
    h = 0
    q = quader(l, b, h)
    assert q.flaeche() == 1
    assert q.umfang() == 4
    assert q.volumen() == 0
