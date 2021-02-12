import copy
import random


def mutation_random_deviation(ind, mu, sigma, p):
    mut = copy.deepcopy(ind)
    for i in range(len(mut)):
        if random.random() < p:
            mut[i] = mut[i] + random.gauss(mu, sigma)
    return mut


random.seed(0)

ind = [random.uniform(0, 10) for _ in range(2)]
mut = mutation_random_deviation(ind, 0, 1, 0.3)

print(f'Original: {ind}')
print(f'Mutated: {mut}')
