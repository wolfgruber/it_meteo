#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Übung 4, Aufgabe 5

import numpy as np
from numpy.random import choice


def evaluate(player1, player2):
    '''Die Funktion wertet einen Spielzug nach den Regeln von 'Schere, Stein,
    Papier' aus. Als Input werden zwei Strings erwartet, das Output ist der
    Spelstand nach dem Zug.'''

    result = np.zeros(2, dtype=int)

    if player1 == "Schere":
        if player2 == "Stein":
            result[1] = 1
        elif player2 == "Papier":
            result[0] = 1

    elif player1 == "Stein":
        if player2 == "Papier":
            result[1] = 1
        elif player2 == "Schere":
            result[0] = 1

    elif player1 == "Papier":
        if player2 == "Schere":
            result[1] = 1
        elif player2 == "Stein":
            result[0] = 1

    return result

# Hier beginnt das Hauptprogramm:
# Die Optionen, aus denen das Programm wählen kann
options = ["Schere", "Stein", "Papier"]

score = np.zeros(2, dtype=int)
game = 0

# Überprüfung, ob das Spiel noch läuft
while score.sum() < 3 or score[0] == score[1]:

    print('\nRunde {}:'.format(game+1))
    human = input('Ihr Spielzug: ')  # Input des Spielers

    try:
        assert human in options
    except AssertionError:  # Überprüfung des Spielzuges
        print("Der Spielzug wurde nicht erkannt.")
        print("Bitte wählen Sie aus 'Schere', 'Stein', 'Papier'.")

    else:
        computer = choice(options)  # Computer wählt einen Zug aus 'options'
        print('Der Computer spielt: '+computer)
        score = score + evaluate(human, computer)  # Der Zug wird ausgewertet
        print('Spielstand: Computer {} : {} Spieler'.format(
            score[1], score[0]))
        game = game + 1  # Rundenzähler

if score[0] < score[1]:  # Ausgabe des Gewinner-/Verlierertextes
    print('\nDer Computer hat {} zu {} gewonnen.'.format(score[1], score[0]))

else:
    print('\nSie haben {} zu {} gewonnen.'.format(score[0], score[1]))
