from path_homology import edgelist_to_graph, H_path

G_1 = [
    '12', '14', '23', '31', '34'
]

G_2 = [
    '12', '13', '14',
    '23', '24', '34'
]

G_3 = [
    '01', '03',
    '12', '31',
    '34', '42'
]

G_4 = [
    '12', '13', '24', '32',
    '43', '53', '54'
]

G = edgelist_to_graph(G_3)

H, C, Diffs, R, Omega = H_path(G, cutoff=3)

print('Dimensions of Omega chain complex C:', C)
print('Dimensions of path homology H:', H)
print('Differentials:')
for i in Diffs:
    print('\n', i)
print('Regular allowed paths:', R)
print('Generators of Omega:', Omega)
