import math
import gudhi as gd
import matplotlib.pyplot as plt


# Punkty persystencji w formacie (dimension, (birth, death))
persistence_pairs = [
    (0, (0, 1)),   # e_{v_4,v_2}
    (0, (0, 2)),   # e_{v_0,v_1}
    (0, (0, 3)),   # e_{v_1,v_2}
    (0, (0, 4)),   # e_{v_3,v_1}
    (0, (0, math.inf)),  # spójna składowa
    (1, (7, 7)),   # e_{v_0,v_3,v_1}
    (1, (10, 10))  # e_{v_3,v_4,v_2} - e_{v_3,v_1,v_2}
]

# Rysowanie diagramu persystencji
gd.plot_persistence_diagram(persistence_pairs)
plt.title("Diagram persystencji")
plt.savefig("diagram_persystencji.pdf", bbox_inches='tight')
plt.show()
plt.close()
