import copy
import random


def mutation_exchange(ind):
    mut = copy.deepcopy(ind)
    pos = random.sample(range(0, len(mut)), 2)
    g1 = mut[pos[0]]
    g2 = mut[pos[1]]
    mut[pos[1]] = g1
    mut[pos[0]] = g2
    return mut


random.seed(1)

ind = list(range(1, 7))
mut = mutation_exchange(ind)

print(f'Original: {ind}')
print(f'Mutated: {mut}')
