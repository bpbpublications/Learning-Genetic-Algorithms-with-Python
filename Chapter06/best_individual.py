import random
from math import sin, cos

from ch6.toolbox import (
    crossover_blend, mutation_random_deviation, selection_tournament, crossover_operation,
    mutation_operation, stats,
    plot_stats,
)


def func(x, y):
    return sin(x) * cos(x) - pow(abs((x + 50) * (y - 10)) / 10, 0.1)


class Individual:

    def __init__(self, gene_list) -> None:
        self.gene_list = gene_list
        self.fitness = func(self.gene_list[0], self.gene_list[1])

    def __str__(self):
        return f'x: {self.gene_list[0]}, y: {self.gene_list[0]}, fitness: {self.fitness}'


def crossover(parent1, parent2):
    child1_genes, child2_genes = crossover_blend(parent1.gene_list, parent2.gene_list, 0.5)
    return Individual(child1_genes), Individual(child2_genes)


def mutate(ind):
    mutated_gene = mutation_random_deviation(ind.gene_list, 0, 1, 0.5)
    return Individual(mutated_gene)


def select(population):
    return selection_tournament(population, group_size = 2)


def create_random():
    return Individual([random.uniform(-100, 100), random.uniform(-100, 100)])


random.seed(28)
POPULATION_SIZE = 10
CROSSOVER_PROBABILITY = .8
MUTATION_PROBABILITY = .1
MAX_GENERATIONS = 25

first_population = [create_random() for _ in range(POPULATION_SIZE)]
population = first_population.copy()
fitness_list = [ind.fitness for ind in population]

fit_avg = [sum(fitness_list) / len(population)]
fit_best = [max(fitness_list)]
fit_best_ever = [max(fitness_list + fit_best)]
best_ind = random.choice(first_population)

generation_number = 0

while generation_number < MAX_GENERATIONS:
    generation_number += 1
    offspring = select(population)
    crossed_offspring = crossover_operation(offspring, crossover, CROSSOVER_PROBABILITY)
    mutated_offspring = mutation_operation(crossed_offspring, mutate, MUTATION_PROBABILITY)
    population = mutated_offspring.copy()
    best_ind, fit_avg, fit_best, fit_best_ever = stats(population, best_ind, fit_avg, fit_best, fit_best_ever)

plot_stats(fit_avg, fit_best, fit_best_ever,
           "Finding maxima of function: \n sin(x) * cos(x) - pow(abs((x + 50) * (y - 10)) / 10, 0.1)")
print(f'Best Individual: {best_ind}')
