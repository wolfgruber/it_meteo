class kreis:
    '''Klasse "Kreis" beschreibt einen geom. Kreis mit einem Radius, der bei
    Initialisierug übergeben wird. Funktionen sind: Umfang und Fläche'''

    pi = 3.141592653589793

    def __init__(self, R):
        '''initialisiert Obj. Kreis'''
        self.Radius = R

    def flaeche(self):
        '''gibt die Fläche des Kreises zurück'''
        return self.pi * self.Radius**2

    def umfang(self):
        '''gibt den Umfang des Kreises zurück'''
        return 2 * self.pi * self.Radius
