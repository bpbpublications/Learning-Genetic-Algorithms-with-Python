import copy
import random


def mutation_bit_flip(ind):
    mut = copy.deepcopy(ind)
    pos = random.randint(0, len(ind) - 1)
    g1 = mut[pos]
    mut[pos] = (g1 + 1) % 2
    return mut


random.seed(21)

ind = [random.randint(0, 1) for _ in range(0, 5)]
mut = mutation_bit_flip(ind)

print(f'Original: {ind}')
print(f'Mutated: {mut}')
