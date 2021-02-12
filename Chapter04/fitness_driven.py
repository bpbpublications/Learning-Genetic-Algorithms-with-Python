import copy
import random
from math import sin, cos


def fitness_function(x, y):
    return sin(x) * cos(y)


class Individual:

    def __init__(self, x, y) -> None:
        self.gene_set = [x, y]
        self.fitness = fitness_function(x, y)

    def __str__(self):
        return f'x: {self.gene_set[0]}, '\
               f'y: {self.gene_set[1]}, '\
               f'fitness: {round(self.fitness, 4)}'


def generate_random():
    return Individual(round(random.random(), 2), round(random.random(), 2))


def crossover_fitness_driven_blend(ind1, ind2, alpha):
    c1 = copy.deepcopy(ind1.gene_set)
    c2 = copy.deepcopy(ind2.gene_set)

    for i in range(len(c1)):
        l = min(c1[i], c2[i]) - alpha * abs(c2[i] - c1[i])
        u = max(c1[i], c2[i]) + alpha * abs(c2[i] - c1[i])
        c1[i] = round(l + random.random() * (u - l), 2)
        c2[i] = round(l + random.random() * (u - l), 2)

    child1 = Individual(c1[0], c1[1])
    child2 = Individual(c1[0], c1[1])

    candidates = [ind1, ind2, child1, child2]

    best = sorted(candidates, key = lambda ind: ind.fitness, reverse = True)

    return best[0:2]


random.seed(3)

p1, p2 = generate_random(), generate_random()

offspring = crossover_fitness_driven_blend(p1, p2, 0.5)

print(f'Parent 1: {p1}')
print(f'Parent 2: {p2}')

print(f'Child 1: {offspring[0]}')
print(f'Child 2: {offspring[1]}')
