from mpmath import zetazero

# rho(n) berechnet die n-te nichttriviale Nullstelle der
# riemannschen Zetafunktion.
# Dazu wird die Bibliothek mpmath mit der Funktion zetazero
# zur Berechnung der Nullstellen herangezogen.

def rho(n, precision = 5):
    for x in range(1, n+1):
        zero = zetazero(x)
        print("\u03C1" + str(x) + " = (" + str(zero.real) + " + " + str(round(zero.imag, precision)) + "i)")
