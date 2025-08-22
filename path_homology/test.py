from path_homology import edgelist_to_graph, H_path

# przykładowe grafy (Twoja baza)
graphs = {
    'G1': ['12', '14', '23', '31', '34'],
    'G2': ['12', '13', '14', '23', '24', '34'],
    'G3': ['01', '03', '31', '21', '42', '43'],
    'G4_cycle_5': ['01', '12', '23', '34', '40'],
    'G5_full_triangle': ['01', '02', '10', '12', '20', '21'],
    'G6': ['12', '13', '24', '32', '43', '53', '54'],
    'G7_two_triangles': ['01', '12', '20', '23', '34', '42'],
    'G8_cycle_4': ['01', '12', '23', '30'],
    'G9_triangle_dense': ['01', '12', '20', '02', '21'],
    'G10_octahedron': [
        '02', '03', '04', '05', '12', '13', '14', '15', '24', '25', '34', '35'
    ]
}

results = []
for name, edges in graphs.items():
    print(f'\n=== {name} ===')
    print('Edges:', edges)

    # konstrukcja grafu i obliczenie homologii z cutoff=4
    G = edgelist_to_graph(edges)
    H, C, Diffs, R, Omega = H_path(G, cutoff=3)

    # podstawowe info
    print('n_vertices):', len(G))
    print('Dimensions of Omega chain complex C:', C)
    print('Dimensions of path homology H:', H)

    # sprawdzenie H1, H2, wypisanie generatorów (jeśli dostępne)
    nonzero = []
    if len(H) > 1 and H[1] != 0:
        nonzero.append(('H1', H[1]))
    if len(H) > 2 and H[2] != 0:
        nonzero.append(('H2', H[2]))

    for p, dim in enumerate(H):
        if dim != 0 and p > 0:
            print(f'\nH_{p} non-zero, dimension {dim}')
            print(f'Generators of Omega_{p}:')
            for i, g in enumerate(Omega[p]):
                print(g)

    if not nonzero:
        print('\nWnioski: H1 = 0 i H2 = 0 (brak niezerowych homologii wyższych stopni)')
