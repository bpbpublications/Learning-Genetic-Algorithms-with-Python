import copy
import random
from math import sin
from typing import List

def func(x):
    return sin(x) - .2 * abs(x)

class Individual:

    def __init__(self, gene_list: List[float]) -> None:
        self.gene_list = gene_list
        self.fitness = func(self.gene_list[0])

    def __str__(self):
        return f'x: {self.gene_list[0]}, fitness: {self.fitness}'


def mutation_fitness_driven_random_deviation(ind, mu, sigma, p, max_tries = 3):
    for t in range(0, max_tries):
        mut_genes = copy.deepcopy(ind.gene_list)
        for i in range(len(mut_genes)):
            if random.random() < p:
                mut_genes[i] = mut_genes[i] + random.gauss(mu, sigma)
        mut = Individual(mut_genes)
        if ind.fitness < mut.fitness:
            return mut
    return ind

random.seed(14)

ind = Individual([random.uniform(-10, 10)])
mut = mutation_fitness_driven_random_deviation(ind, 0, 1, 3)

print(f'Original: ({ind})')
print(f'Mutated: ({mut})')
