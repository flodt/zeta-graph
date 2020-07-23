import matplotlib.pyplot as plt
import pylab
import os
from mpmath import cplot, zeta

# compley-plot.py zeichnet den eingefaerbten komplexen Graphen der
# Riemannschen Zetafunktion im Bereich Re(s) zwischen -15 und 15,
# und Im(s) zwischen -23 und 23. Dazu werden 10 Millionen einzelne
# Punkte betrachtet. Die Generierung beansprucht circa 3,5 Stunden.
# Zum Vergleich wird die Funktion f(z) = z betrachtet, die die
# Technik des Einfaerbens erklaeren soll.

#cplot(zeta, [-15,15], [-23,23], points=10000000, file='complex-plot.pdf', verbose=True)
#cplot(zeta, [-5,2.5], [-5,5], points=10000000, file='complex-plot-small.pdf', verbose=True)
#cplot(zeta, [-5,2.5], [-40,40], points=10000000, file='complex-plot-large.pdf', verbose=True)
#cplot(zeta, [-18,18], [-18,18], points=10000000, file='complex-plot-extended.pdf', verbose=True)
#os.system('open complex-plot.pdf')

#cplot(lambda z: z, [-5,5], [-5,5], points=500000, file='complex-plot-z.pdf', verbose=True)
#cplot(lambda z: z**2, [-5,5], [-5,5], points=500000, file='complex-plot-z2.pdf', verbose=True)
cplot(lambda z: (z**2)+1, [-5,5], [-5,5], points=500000, file='complex-plot-z2+1.pdf', verbose=True)