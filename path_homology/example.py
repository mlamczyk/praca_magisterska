# -*- coding: utf-8 -*-

from path_homology import edgelist_to_graph, H_path

commuting_square = [
    'ab', 'bd', 'ac', 'cd',
]

octahedron = [  # Example 1.27
    '01','21','03','23',
    'a0','a1','a2','a3',
    'b0','b1','b2','b3'
]

cube = [
    'ab', 'ac', 'bd', 'cd',
    'ef', 'eg', 'gh', 'fh',
    'ae', 'bf', 'cg', 'dh'
]

hollow_2x2x2_cube = [ # Example 1.30
    'ab', 'bc', 'de', 'ef', 'gh', 'hi',
    'ad', 'dg', 'be', 'eh', 'cf', 'fi',
    'jk', 'kl', 'op', 'pq',
    'jm', 'mo', 'ln', 'nq',
    'rs', 'st', 'uv', 'vw', 'xy', 'yz',
    'ru', 'ux', 'sv', 'vy', 'tw', 'wz',
    'rj', 'ja', 'um', 'md', 'xo', 'og',
    'tl', 'lc', 'wn', 'nf', 'zq', 'qi',
    'sk', 'kb',
    'yp', 'ph',
]

exotic_sphere = [ # Theorem 6.1 of https://arxiv.org/pdf/1803.07497.pdf
        '12', '13', '14', '15',
        '26', '27', '36', '38', '47', '49', '58', '59',
        '60', '70', '80', '90'
]

G_1 = [
    '12', '14', '23', '31', '34'
]

G_2 = [
    '12', '13', '14',
    '23', '24', '34'
]

G_3 = [
    '12', '13', '24', '32',
    '43', '53', '54'
]

G = edgelist_to_graph(G_3)

H, C, Diffs, R, O = H_path(G, cutoff=3)

print('Dimensions of Omega chain complex C:', C)
print('Dimensions of path homology H:', H)
print('Differentials:')
for i in Diffs:
    print('\n', i)
print('Regular allowed paths:', R)
print('Generators of Omega:', O)



