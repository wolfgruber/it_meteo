from class_formen import formen
from rechteck import rechteck

class quader(rechteck):
    """Quader-Klasse repräsentiert einen Quader und ist aus einem Rechteck mit
    einer Höhe aufgebaut. Der Quader erbt die Funktionen flaeche() und
    umfang() von seiner Basisklasse rechteck"""

    def __init__(self, L, B, H):
        self.Laenge = self.check_input(L)
        self.Breite = self.check_input(B)
        self.Hoehe = self.check_input(H)

    def volumen(self):
        """Gibt das Volumen des Quaders zurück. Basiert auf der
        flaeche()-Funktion von rechteck"""
        return self.flaeche() * self.Hoehe
