import random
from typing import List
from numpy import arange
import matplotlib.pyplot as plt
from pylab import meshgrid, cm

from ch7.toolbox import (
    crossover_blend, mutation_random_deviation, constraints, selection_rank_with_elite,
    crossover_operation,
    mutation_operation,
)


def func(x, y):
    return - 10 * (pow(x, 5) / (3 * pow(x * x * x / 4 + 1, 2) + pow(y, 4) + 10) + pow(x * y / 2, 2) / 1000)


class Individual:
    counter = 0

    def __init__(self, gene_list: List[float]) -> None:
        self.gene_list = [constraints(g) for g in gene_list]
        self.fitness = round(func(self.gene_list[0], self.gene_list[1]), 2)
        self.__class__.counter += 1
        self.id = self.__class__.counter

    def __str__(self):
        return f'x: {self.gene_list[0]}, y: {self.gene_list[0]}, fitness: {self.fitness}'


def crossover(parent1, parent2):
    child1_genes, child2_genes = crossover_blend(parent1.gene_list, parent2.gene_list, 0.8)
    return Individual(child1_genes), Individual(child2_genes)


def mutate(ind):
    mutated_gene = mutation_random_deviation(ind.gene_list, 0, 1, 0.5)
    return Individual(mutated_gene)


def select(population):
    return selection_rank_with_elite(population, elite_size = 2)


def create_random():
    return Individual([round(random.uniform(-10, 10), 2), round(random.uniform(-10, 10), 2)])


x = arange(-10.0, 10.0, 0.1)
y = arange(-10.0, 10.0, 0.1)
X, Y = meshgrid(x, y)
Z = func(X, Y)

random.seed(63)
POPULATION_SIZE = 16
CROSSOVER_PROBABILITIES = [.0, .4, .7]
MUTATION_PROBABILITY = .2
MAX_GENERATIONS = 10

for CROSSOVER_PROBABILITY in CROSSOVER_PROBABILITIES:
    first_population = [create_random() for _ in range(POPULATION_SIZE)]
    best_individual = random.choice(first_population)
    generation_number = 0

    population = first_population.copy()

    while generation_number < MAX_GENERATIONS:
        generation_number += 1
        offspring = select(population)
        crossed_offspring = crossover_operation(offspring, crossover, CROSSOVER_PROBABILITY)
        mutated_offspring = mutation_operation(crossed_offspring, mutate, MUTATION_PROBABILITY)
        population = mutated_offspring.copy()

        best_of_generation = max(population, key = lambda ind: ind.fitness)
        if best_individual.fitness < best_of_generation.fitness:
            best_individual = best_of_generation

        im = plt.imshow(Z, cmap = cm.bwr, extent = [-10, 10, -10, 10])
        plt.colorbar(im)
        plt.xticks([])
        plt.yticks([])
        plt.title(f"Crossover Probability: {CROSSOVER_PROBABILITY}, Generation: {generation_number} \n"
                  f"Best Individual: {best_individual.fitness}")
        plt.scatter([ind.gene_list[0] for ind in population],
                    [ind.gene_list[1] for ind in population],
                    color = 'black')
        plt.show()

    print(f'Best Individual : {best_individual} for crossover probability: {CROSSOVER_PROBABILITY}')
