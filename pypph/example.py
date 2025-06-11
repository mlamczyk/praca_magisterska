import sys
from pphTools import Dirnet
import matplotlib.pyplot as plt
import gudhi as gd
import numpy as np


fn = sys.argv.pop()
dn = Dirnet(fn)

# H_0: wierzchołki, wszystkie istnieją od czasu 0
# H_1: pewne ścieżki o długości 1, nie powinny mieć czasu śmierci 1000.0
# (0.0, 1.0) oznacza, że wierzchołek urodził się przy wartości 0 i zniknął (połączył się z innym) przy wartości 1
# (0.0, 10000.0) cecha ta nigdy nie zanika w obrębie rozważanej filtracji

# Konwersja 10000.0 do np.infty i do listy (dim, (birth, death_val)
diagram = []
for i, (desc, bars) in enumerate(dn.pers):
    dim = i
    print(dim, desc, bars)
    for birth, death in bars:
        if death == 10000.0:
            death_val = np.inf
        else:
            death_val = death
        diagram.append((dim, (birth, death_val)))

gd.plot_persistence_diagram(diagram)
plt.show()
