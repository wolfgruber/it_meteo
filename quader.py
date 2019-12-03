from class_formen import formen
from rechteck import rechteck

class quader(rechteck):
    """..."""
    def volumen(self, Hoehe):
        return self.flaeche() * Hoehe
