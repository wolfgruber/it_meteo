import numpy as np

from rechteck import rechteck
from kreis import kreis


def wuerfel():
    '''gibt eine gleichmäßig verteilte Zufallszahl aus [1,50] zurück'''
    return np.random.randint(1, 51)


re = rechteck(2, 5)
kr = kreis(1)

print('Rechteck: Umfang = {:.2f}, Fläche = {:.2f}'
      .format(re.umfang(), re.flaeche()))
print('Kreis:    Umfang = {:.2f}, Fläche = {:.2f}'
      .format(kr.umfang(), kr.flaeche()))

forms = []

for i in range(10):
    choose = np.random.randint(2)

    if choose == 1:
        newmember = rechteck(wuerfel(), wuerfel())

    else:
        newmember = kreis(wuerfel())

    forms.append(newmember)

kr_fl = 0
kr_um = 0
kr_n = 0
re_fl = 0
re_um = 0
re_n = 0

for obj in forms:
    if type(obj) == rechteck:
        re_fl = re_fl + obj.flaeche()
        re_um = re_um + obj.umfang()
        re_n = re_n + 1

    else:
        kr_fl = kr_fl + obj.flaeche()
        kr_um = kr_um + obj.umfang()
        kr_n = kr_n + 1

print('Es wurden {} Kreise und {} Rechtecke erstellt.'.format(kr_n, re_n))

print('Durchschnittliche Fläche der Rechtecke: ' +
      '{:.2f}, durchschnittlicher Umfang: {:.2f}'
      .format(re_fl/re_n, re_um/re_n))

print('Durchschnittliche Fläche der Kreise: ' +
      '{:.2f}, durchschnittlicher Umfang: {:.2f}'
      .format(kr_fl/kr_n, kr_um/kr_n))
