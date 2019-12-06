class formen:
    """Basisklasse für geom. Formen. Enthält leere Funktionen zur Berechnung
    von Fläche, Umfang und Volumen"""
    
    def flaeche(self):
        return

    def umfang(self):
        return

    def volumen(self):
        print('Die Berechnung von Volumen ist noch nicht näher spezifiziert.')
        return
        
    def check_input(self, inpt):
        try:
            assert inpt >= 0
            
        except AssertionError:
            print('Das Input ist darf nicht negativ sein.'+
                  ' Fahre mit Betrag |{}| fort.'.format(inpt))
            return (-inpt)
            
        else:
            return inpt

