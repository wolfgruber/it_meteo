from class_formen import formen

class rechteck(formen):
    '''Klasse "Rechteck" beschreibt ein geom. Rechteck mit den Parametern
    Länge und Breite. Funktionen: Fläche und Umfang. Erbt Funktionen von der
    Klasse formen'''

    def __init__(self, L, B):
        self.Laenge = L
        self.Breite = B

    def flaeche(self):
        '''gibt die Fläche des Rechtecks zurück'''
        return self.Laenge * self.Breite

    def umfang(self):
        '''gibt den Umfang des Rechtecks zurück'''
        return 2 * (self.Laenge + self.Breite)
