import random
from typing import List
import numpy as np
import matplotlib.pyplot as plt

from ch6.toolbox import (
    crossover_blend, mutation_random_deviation, selection_tournament, crossover_operation,
    mutation_operation,
)


def func(x):
    return np.sin(x) - .2 * abs(x)


class Individual:
    counter = 0

    def __init__(self, gene_list: List[float]) -> None:
        self.gene_list = gene_list
        self.fitness = func(self.gene_list[0])
        self.__class__.counter += 1

    def get_gene(self):
        return self.gene_list[0]


def crossover(parent1, parent2):
    child1_gene, child2_gene = crossover_blend([parent1.get_gene()], [parent2.get_gene()], 0.5)
    return Individual(child1_gene), Individual(child2_gene)


def mutate(ind):
    mutated_gene = mutation_random_deviation([ind.get_gene()], 0, 1, 1)
    return Individual(mutated_gene)


def select(population):
    return selection_tournament(population)


def create_random():
    return Individual([random.uniform(-10, 10)])


random.seed(2)
POPULATION_SIZE_LIST = range(10, 35, 5)
NUMBER_OF_RUNS = 500
CROSSOVER_PROBABILITY = .8
MUTATION_PROBABILITY = .1
MAX_GENERATIONS = 10

for POPULATION_SIZE in POPULATION_SIZE_LIST:

    best_fitness_list = []
    number_of_individuals = []

    for run in range(NUMBER_OF_RUNS):

        Individual.counter = 0

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

        best_fitness_list.append(best_individual.fitness)
        number_of_individuals.append(Individual.counter)

    plt.scatter(best_fitness_list, number_of_individuals,
                label = f"Distribution for POPULATION SIZE = {POPULATION_SIZE}")

plt.xlabel('Best Fitness')
plt.ylabel('Number of Individuals')
plt.legend(loc = "upper left")
plt.show()
