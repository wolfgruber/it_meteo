from rechteck import rechteck

def test_rechteck():
    """Funktion zum Testen der rechteck-Klasse"""
    a = 1
    b = 1
    r = rechteck(a, b)
    assert r.flaeche() == 1
    assert r.umfang() == 4

    a = 0.5
    b = 1.5
    r = rechteck(a, b)
    assert r.flaeche() == 0.75
    assert r.umfang() == 4

    a = 0
    b = 1
    r = rechteck(a, b)
    assert r.flaeche() == 0
    assert r.umfang() == 2

    a = 0
    b = 0
    r = rechteck(a, b)
    assert r.flaeche() == 0
    assert r.umfang() == 0

    return
