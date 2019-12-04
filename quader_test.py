from quader import quader

def test_quader():
    l = 1
    b = 1
    h = 1
    q = quader(l, b)
    assert q.flaeche() == 1
    assert q.umfang() == 4
    assert q.volumen(h) == 1
