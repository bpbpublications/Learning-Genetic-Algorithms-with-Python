import copy
import random


def mutation_shuffle(ind):
    mut = copy.deepcopy(ind)
    pos = sorted(random.sample(range(0, len(mut)), 2))
    subrange = mut[pos[0]:pos[1] + 1]
    random.shuffle(subrange)
    mut[pos[0]:pos[1] + 1] = subrange

    return mut


random.seed(13)

ind = list(range(1, 6))
mut = mutation_shuffle(ind)

print(f'Original: {ind}')
print(f'Mutated: {mut}')
