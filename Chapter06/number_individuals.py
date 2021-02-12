import random
from math import sin, cos
from typing import List
import matplotlib.pyplot as plt

from ch6.toolbox import crossover_blend, mutation_random_deviation, selection_tournament


def func(x, y):
    return sin(x) * cos(x) - pow(abs((x + 50) * (y - 10)) / 10, 0.1)


class Individual:
    counter = 0

    def __init__(self, gene_list: List[float]) -> None:
        self.gene_list = gene_list
        self.fitness = func(self.gene_list[0], self.gene_list[1])
        self.__class__.counter += 1

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

stats_fitness_average = []
stats_fitness_best = []
stats_fitness_best_ever = []
stats_number_of_individuals = []
best_individual = random.choice(first_population)

generation_number = 0

population = first_population.copy()

fitness_list = [ind.fitness for ind in population]
stats_fitness_average.append(sum(fitness_list) / len(population))
stats_fitness_best.append(max(fitness_list))
stats_fitness_best_ever.append(max(fitness_list + stats_fitness_best_ever))

while generation_number < MAX_GENERATIONS:

    generation_number += 1

    # SELECTION
    offspring = select(population)

    # CROSSOVER
    crossed_offspring = []
    for ind1, ind2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < CROSSOVER_PROBABILITY:
            kid1, kid2 = crossover(ind1, ind2)
            crossed_offspring.append(kid1)
            crossed_offspring.append(kid2)
        else:
            crossed_offspring.append(ind1)
            crossed_offspring.append(ind2)

    # MUTATION
    mutated_offspring = []
    for mutant in crossed_offspring:
        if random.random() < MUTATION_PROBABILITY:
            new_mutant = mutate(mutant)
            mutated_offspring.append(new_mutant)
        else:
            mutated_offspring.append(mutant)

    population = mutated_offspring.copy()

    fitness_list = [ind.fitness for ind in population]
    best_of_generation = max(population, key = lambda ind: ind.fitness)
    if best_individual.fitness < best_of_generation.fitness:
        best_individual = best_of_generation
    stats_fitness_average.append(sum(fitness_list) / len(population))
    stats_fitness_best.append(max(fitness_list))
    stats_fitness_best_ever.append(max(fitness_list + stats_fitness_best_ever))

plt.plot(stats_fitness_average, label = "Average Fitness of Generation")
plt.plot(stats_fitness_best, label = "Best Fitness of Generation")
plt.plot(stats_fitness_best_ever, label = "Best Fitness Ever")
plt.title("Finding maxima of function: \n sin(x) * cos(x) - pow(abs((x + 50) * (y - 10)) / 10, 0.1)")
plt.legend(loc = "lower right")
plt.show()

print(f'Best Individual: {best_individual}')
print(f'Total Number of Individuals: {Individual.counter}')
