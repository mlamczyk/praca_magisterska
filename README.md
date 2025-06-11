# Skrypty wykorzystane w pracy magisterskiej ,,Homologie ścieżek dla grafów skierowanych''

Przykłady obliczania homologii ścieżek i persystentnych homologii ścieżek.

## Jak uruchomić ten projekt

Po sklonowaniu repozytorium skonfiguruj środowisko wirtualne i zainstaluj niezbędne wymagania:
```
python -m venv venv 
venv\Scripts\activate
pip install -r requirements.txt
```

Przykłady podzielono na implementacje pochodzące z różnych repozytoriów. Kody źródłowe pochodzą od cytowanych autorów i zostały zmodyfikowane w niewielkim stopniu lub wcale.

---

### PathHom
Kod Pythona dotyczący homologii ścieżek i persystentnych homologii ścieżek. Zwraca liczby Bettiego oraz zbiory dopuszczalnych ścieżek stopnia od 0 do p. \
Repozytorium: https://github.com/WeilabMSU/PathHom \
Kod oparty jest na pracy autorów: Chen, D., Liu, J., & Weilab at MSU Math. (2022) [zob. cytowanie poniżej].

Aby uruchomić przykładowy plik `pathHom\example.py`, należy przygotować graf wejściowy w postaci dwóch obiektów NumPy:
- `nodes = numpy.array([1, 2, 3])` – lista numerów wierzchołków,
- `edges = numpy.array([[1, 2], [2, 3]])` - lista skierowanych krawędzi jako tablica par wierzchołków.

Następnie wystarczy uruchomić:
```
python pathHom\example.py
```

---

### path_homology
Skrypt Pythona do obliczania homologii ścieżek grafów skierowanych. Zwraca:
- wymiary przestrzeni Omega (przestrzeni niezmienniczych ścieżek),
- liczby Bettiego (wymiary grup homologii),
- macierze brzegowe,
- regularne dopuszczalne ścieżki,
- generatory przestrzeni Omega.

Repozytorium: https://github.com/sheaves/path_homology \
Kod oparty jest na pracy autorów: Carranza, Doherty, Kapulkin, Opie, Sarazola i Wong (2022) [zob. cytowanie poniżej].

Aby uruchomić przykładowy plik `path_homology\example.py` z własnym grafem, należy zastąpić zmienną `G_2` w miejscu
```
G = edgelist_to_graph(G_2)
```
swoją listą krawędzi w formacie ciągów dwuliterowych, np.:
```
graph = ['ab', 'bd', 'ac', 'cd']
```
Każdy element listy to dwuliterowy string reprezentujący skierowaną krawędź (np. `'ab'` to krawędź z wierzchołka `a` do `b`).

Uruchomienie:
```
python path_homology\example.py
```

---

### pypph
Implementacja pakietu Persistent Path Homology (PPH). Zwraca pary narodzin i śmierci klas homologii dla wymiarów 0 i 1. Wartość 10000 oznacza nieskończoność i powinna pojawić się tylko w przypadku 0-wymiarowym. Nieskończenie długie paski 0-wymiarowe reprezentują połączone komponenty, które żyją wiecznie. \
Repozytorium: https://github.com/samirchowdhury/pypph \
Kod oparty jest na pracy autorów: Chowdhury, S., & Mémoli, F. (2018) [zob. cytowanie poniżej].

Aby uruchomić plik `pypph\example.py` dla własnego grafu, należy przygotować plik `.txt` w formacie:
- pierwszy wiersz: liczba wierzchołków,
- kolejne wiersze: trzy kolumny – początek krawędzi, koniec krawędzi, waga (np. `1 2 1.0` oznacza krawędź z 1 do 2 o wadze 1.0).

Przykład zawartości pliku `pypph\graph.txt`:
```
3
1 2 1.0
2 3 4.0
```

Uruchomienie:
```
python pypph\example.py pypph\graph.txt
```

---

## Cytowanie

Jeśli wykorzystujesz kod `PathHom\pathhomology.py`, proszę zacytuj:

Chen, D., Liu, J., & Weilab at MSU Math. (2022). PathHom: Persistent path topology in molecular and materials sciences. https://github.com/WeilabMSU/PathHom \
Zob. także publikację: \
Chen, D., Liu, J., & Wei, G.-W. (2022). Persistent path topology in molecular and materials sciences. Nature Computational Science, 2, 139–150. https://doi.org/10.1038/s43588-022-00208-2

Jeśli wykorzystujesz kod `path_homology\path_homology.py`, proszę zacytuj:

Carranza, D., Doherty, B., Kapulkin, K., Opie, M., Sarazola, M., & Wong, L. Z. (2022). Python script for computing path homology of digraphs (Version 1.0.0). https://github.com/sheaves/path_homology \
Zob. także publikację: \
Carranza, D., Doherty, B., Kapulkin, K., Opie, M., Sarazola, M., & Wong, L. Z. (2022). Cofibration Category of Digraphs for Path Homology. arXiv:2212.12568 [math.AT]. https://arxiv.org/abs/2212.12568

Jeśli wykorzystujesz kod `pypph\pphTools.py`, proszę zacytuj:

Chowdhury, S., & Mémoli, F. (2018). Persistent Path Homology of Directed Networks. In Proceedings of the Twenty-Ninth Annual ACM-SIAM Symposium on Discrete Algorithms (SODA), 1152–1169. https://doi.org/10.1137/1.9781611975031.74 \
Kod źródłowy: https://github.com/samirchowdhury/pypph
