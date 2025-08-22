import numpy as np
from pathhomology import PathHomology

nodes1 = np.array([1, 2, 3, 4])
edges1 = np.array(
    [
        [1, 2],
        [1, 4],
        [2, 3],
        [3, 1],
        [3, 4]
    ]
)

nodes2 = np.array([1, 2, 3, 4])
edges2 = np.array(
    [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 4]
    ]
)

nodes3 = np.array([0, 1, 2, 3, 4])
edges3 = np.array(
    [
        [0, 1],
        [0, 3],
        [3, 1],
        [2, 1],
        [4, 2],
        [4, 3]
    ]
)

nodes = np.array([1, 2, 3, 4, 5, 6])
edges = np.array(
    [
        [1, 2],
        [2, 3],
        [2, 4],
        [3, 1],
        [3, 5],
        [4, 5],
        [4, 6],
        [6, 5]
    ]
)

max_path = 2

print('\nGraph G_1')
betti_num1, allowed_paths1 = PathHomology().path_homology(edges1, nodes1, max_path)
print(f'Betti numbers for 0 to max {max_path} path: {betti_num1}')
print(f'Allowed paths: {allowed_paths1}')

print('\nGraph G_2')
betti_num2, allowed_paths2 = PathHomology().path_homology(edges2, nodes2, max_path)
print(f'Betti numbers for 0 to max {max_path} path: {betti_num2}')
print(f'Allowed paths: {allowed_paths2}')

print('\nGraph G_3')
betti_num3, allowed_paths3 = PathHomology().path_homology(edges3, nodes3, max_path)
print(f'Betti numbers for 0 to max {max_path} path: {betti_num3}')
print(f'Allowed paths: {allowed_paths3}')

print('\nGraph G')
betti_num, allowed_paths = PathHomology().path_homology(edges, nodes, max_path)
print(f'Betti numbers for 0 to max {max_path} path: {betti_num}')
print(f'Allowed paths: {allowed_paths}')
