import copy
import random


def mutation_inversion(ind):
    mut = copy.deepcopy(ind)
    temp = copy.deepcopy(ind)
    pos = sorted(random.sample(range(0, len(mut)), 2))
    for i in range(0, (pos[1] - pos[0]) + 1):
        mut[pos[0] + i] = temp[pos[1] - i]

    return mut


random.seed(5)

ind = list(range(1, 6))
mut = mutation_inversion(ind)

print(f'Original: {ind}')
print(f'Mutated: {mut}')
