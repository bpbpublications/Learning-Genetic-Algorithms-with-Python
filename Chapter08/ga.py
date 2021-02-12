import copy
import random

from ch8.functions import complicated_one
from ch8.toolbox import (
    crossover_blend, mutation_random_deviation, selection_rank_with_elite, crossover_operation,
    mutation_operation,
    stats,
    plot_stats,
)


def closest(value, value_list):
    return min(value_list, key = lambda x: abs(x - value))


def range_limit(g, min_v, max_v):
    return max(min(g, max_v), min_v)


class Individual:
    counter = 0
    n_set = range(0, 21)
    func_set = ['sin', 'cos']

    def __init__(self, gene_list):
        self.__class__.counter += 1
        a_raw, b_raw, x_raw, n_raw, func_name = gene_list
        self.gene_list = [
            range_limit(a_raw, 0, 1),
            range_limit(b_raw, 0, 1),
            range_limit(x_raw, -100, 100),
            closest(n_raw, self.n_set),
            func_name
        ]

        a, b, x, n, func_name = self.gene_list
        self.fitness = complicated_one(a, b, x, n, func_name)


def create_random():
    return Individual([
        random.uniform(0, 1),
        random.uniform(0, 1),
        random.uniform(-10, 10),
        random.choice(Individual.n_set),
        random.choice(Individual.func_set)
    ])


def crossover(p1, p2):
    prob = .5
    a1, b1, x1, n1, func_name1 = copy.deepcopy(p1.gene_list)
    a2, b2, x2, n2, func_name2 = copy.deepcopy(p2.gene_list)

    if random.random() < prob:
        a1, a2 = crossover_blend(a1, a2, 0.3)

    if random.random() < prob:
        b1, b2 = crossover_blend(b1, b2, 0.5)

    if random.random() < prob:
        x1, x2 = crossover_blend(x1, x2, 1)

    if random.random() < prob:
        n1, n2 = crossover_blend(n1, n2, 0.5)

    if random.random() < prob:
        func_name1, func_name2 = func_name2, func_name1

    return Individual([a1, b1, x1, n1, func_name1]), Individual([a2, b2, x2, n2, func_name2])


def mutate(ind):
    prob = .5
    a, b, x, n, func_name = copy.deepcopy(ind.gene_list)
    if random.random() < prob:
        a = mutation_random_deviation(a, 0, .2, 1)

    if random.random() < prob:
        b = mutation_random_deviation(b, 0, .2, 1)

    if random.random() < prob:
        x = mutation_random_deviation(x, 0, 1, 1)

    if random.random() < prob:
        n = mutation_random_deviation(n, 0, 1, 1)

    if random.random() < prob:
        func_name = random.choice(Individual.func_set)

    return Individual([a, b, x, n, func_name])


random.seed(19)
POPULATION_SIZE = 200
CROSSOVER_PROBABILITY = .8
MUTATION_PROBABILITY = .2
MAX_GENERATIONS = 1_000

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
    offspring = selection_rank_with_elite(population, elite_size = 3)
    crossed_offspring = crossover_operation(offspring, crossover, CROSSOVER_PROBABILITY)
    mutated_offspring = mutation_operation(crossed_offspring, mutate, MUTATION_PROBABILITY)
    population = mutated_offspring.copy()

    best_ind, fit_avg, fit_best, fit_best_ever = stats(population, best_ind, fit_avg, fit_best, fit_best_ever)

plot_stats(fit_avg, fit_best, fit_best_ever, "Genetic Algorithm Flow")

print(f'Maximum: {best_ind.fitness}')
print(f'Best Individual : {best_ind.gene_list}')
print(f'Number of Individuals: {Individual.counter}')
