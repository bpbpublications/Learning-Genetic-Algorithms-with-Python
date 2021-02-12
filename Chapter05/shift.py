import copy
import random
from math import copysign


def mutation_shift(ind):
    mut = copy.deepcopy(ind)
    pos = random.sample(range(0, len(mut)), 2)
    g1 = mut[pos[0]]
    dir = int(copysign(1, pos[1] - pos[0]))
    for i in range(pos[0], pos[1], dir):
        mut[i] = mut[i + dir]
    mut[pos[1]] = g1
    return mut


random.seed(21)

ind = list(range(1, 6))
mut = mutation_shift(ind)

print(f'Original: {ind}')
print(f'Mutated: {mut}')
