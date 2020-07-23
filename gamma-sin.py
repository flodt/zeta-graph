# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from mpmath import gamma, sin, pi
import pylab

# gamma-sin.py zeichnet die Funktion sin(0.5 * pi * s) und die Funktion
# gamma(1-s) in ein reelles Koordinatensystem. Hierbei soll die
# Überlappung der Positionen der Nullstellen der Sinusfunktion und der
# Polstellen der Gammafunktion gezeigt werden.

x = np.arange(-6,6,0.01)
sine = []
gamma_rev = []

for k in x:
    sine.append(sin(0.5 * pi * k))

for j in x:
    if abs(gamma(-j)) > 10000:
        gamma_rev.append(np.nan)
        continue
    gamma_rev.append(gamma(-j))

plt.axhline(0, color='black', alpha=1, linewidth=1)
for k in [2,4]:
    plt.axvline(k, color='grey', alpha=0.7, linewidth=1, linestyle='dashed')

plt.plot(x, sine, color='blue', label=r'$\sin\left(\frac{\pi s}{2}\right)$', linewidth=3)
plt.plot(x, gamma_rev, color='red', label=r'$\Gamma(1-s)$', linewidth=3)

plt.xlim(-5,5)
plt.ylim(-5,5)
plt.xlabel("s")
plt.ylabel("y")
plt.legend(loc='lower left')

pylab.savefig('gamma-sin.pdf')
