from matplotlib import pyplot as plt
from mpmath import zeta, zetazero
import numpy as np
import pylab

# critical-line.py zeichnet Wert des Betrages der
# Zetafunktion über t nach Einsetzen der komplexen Zahlen
# s = (0.5 + i t). Dies zeigt das Verhalten der Funktion
# entlang der kritischen Geraden.

t = np.arange(-26,26,0.01)
absolute = []

for k in t:
    absolute.append(float(abs(zeta(complex(0.5, k)))))

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 13
fig_size[1] = 6
plt.rcParams["figure.figsize"] = fig_size

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

for k in [1,2]:
    zero = zetazero(k).imag
    plt.axvline(zero, color='grey', alpha=1, linewidth=1, linestyle='dashed')
    plt.axvline(zero*(-1), color='grey', alpha=1, linewidth=1, linestyle='dashed')

plt.plot(t, absolute, color='red', linewidth=3, label=r'$\left|\zeta\left(\frac{1}{2} + i t\right)\right|$')

plt.xlim(-24,24)
plt.ylim(-0.4,3)
plt.xlabel("t")
plt.ylabel(r"$\left|\zeta\left(\frac{1}{2} + i t\right)\right|$")
plt.legend(loc='best')
plt.grid(True)

pylab.savefig("critical-line-abs.pdf")
