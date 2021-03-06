import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from mpmath import zetazero
import pylab

fix, ax = plt.subplots()

plt.axhline(0, color='black', alpha=1, linewidth=1)
plt.axvline(0, color='black', alpha=1, linewidth=1)

ax.add_patch(patches.Rectangle((1,-8), 7, 16, color='green', fill=True, linewidth=1, alpha=0.3, zorder=0, label=r'$\operatorname{Re}(s) > 1$'))
ax.add_patch(patches.Rectangle((-8,-8), 8, 16, color='orange', fill=True, linewidth=1, alpha=0.3, zorder=0, label=r'$\operatorname{Re}(s) < 0$'))
ax.add_patch(patches.Rectangle((0,-8), 1, 16, color='red', fill=True, linewidth=1, alpha=0.3, zorder=0, label=r'Kritischer Streifen $0 < \,\operatorname{Re}(s) < 1$'))

plt.xlim(-8,8)
plt.ylim(-8,8)
plt.xlabel("Re(s)")
plt.ylabel("Im(s)")
plt.legend(loc='upper left')

pylab.savefig('zeta-areas.pdf')
