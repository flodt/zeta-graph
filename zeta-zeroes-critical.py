import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from mpmath import zetazero
import pylab

# zeta-zeroes-info.py zeichnet eine komplexe Zahlenebene, in der
# die Nullstellen der Zetafunktion dargestellt werden.

fix, ax = plt.subplots()

re_nontrivial = []
im_nontrivial = []

for j in range(0,6):
    re_nontrivial.append(zetazero(j+1).real)
    im_nontrivial.append(zetazero(j+1).imag)
    re_nontrivial.append(zetazero(j+1).real)
    im_nontrivial.append(-zetazero(j+1).imag)

plt.axhline(0, color='black', alpha=1, linewidth=1)
plt.axvline(0, color='black', alpha=1, linewidth=1)
plt.axvline(0.5, color='black', alpha=1, linewidth=1, linestyle='dashed', label=r'Kritische Gerade $\operatorname{Re}(s)=\frac{1}{2}$')
ax.add_patch(patches.Rectangle((0,-40), 1, 80, color='red', fill=True, linewidth=1, alpha=0.3, zorder=0, label=r'Kritischer Streifen $0 < \,\operatorname{Re}(s) < 1$'))

plt.scatter(re_nontrivial, im_nontrivial, color='red', label='Nichttriviale Nullstellen', zorder=10)

for m in range(0, len(re_nontrivial)):
    if im_nontrivial[m] > 0:
        text = '(0.5 + ' + str(abs(round(im_nontrivial[m], 3))) + 'i)'
    else:
        text = '(0.5 - ' + str(abs(round(im_nontrivial[m], 3))) + 'i)'
    ax.annotate(text, xy=(re_nontrivial[m], im_nontrivial[m]), xycoords='data', xytext=(re_nontrivial[m]+0.58, im_nontrivial[m]-0.6), arrowprops=dict(arrowstyle="->"))

plt.xlim(-5,2.8)
plt.ylim(-40,40)
plt.xlabel("Re(s)")
plt.ylabel("Im(s)")
plt.legend(loc='best')

pylab.savefig('zeta-zeroes-critical-all.pdf')
