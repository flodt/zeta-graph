from mpmath import zeta, plot, gamma, sin, pi

# real-plot.py zeichnet zwei reelle Graphen der Riemannschen
# Zetafunktion. Der Graph wird erst im Bereich mit x zwischen -4 und
# 6 betrachtet, dann mit x zwischen -49 und 51.

plot(zeta, [-4,6], ylim=[-20,20], points=1000, file="real-plot-1.pdf", singularities=[1])
plot(zeta, [-49,51], ylim=[-20,20], points=10000, file="real-plot-2.pdf", singularities=[1])
