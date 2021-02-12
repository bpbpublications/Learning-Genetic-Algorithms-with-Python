import random

from ch10.tsp.individual import Individual, generate_random
from ch10.tsp.route import get_us_capitals, plot_route
from ch10.tsp.toolbox import (
    crossover_fitness_driven_order, mutation_fitness_driven_shift, selection_rank_with_elite,
    crossover_operation,
    stats,
    mutation_operation,
    plot_stats,
)


def crossover(parent1, parent2):
    return crossover_fitness_driven_order(parent1, parent2)


def mutate(ind):
    return mutation_fitness_driven_shift(ind)


def select(population):
    return selection_rank_with_elite(population, elite_size = 2)


points = get_us_capitals()
Individual.points = points

random.seed(60)

POPULATION_SIZE = 200
CROSSOVER_PROBABILITY = .3
MUTATION_PROBABILITY = .9
MAX_GENERATIONS = 300

first_population = [generate_random(len(points)) for _ in range(POPULATION_SIZE)]
best_ind = random.choice(first_population)
fit_avg = []
fit_best = []
generation_num = 0
population = first_population.copy()

while generation_num < MAX_GENERATIONS:
    generation_num += 1
    offspring = selection_rank_with_elite(population, elite_size = 2)
    crossed_offspring = crossover_operation(offspring, crossover, CROSSOVER_PROBABILITY)
    mutated_offspring = mutation_operation(crossed_offspring, mutate, MUTATION_PROBABILITY)
    population = mutated_offspring.copy()
    best_ind, fit_avg, fit_best = stats(population, best_ind, fit_avg, fit_best)
    print(f'{generation_num}: {fit_avg[-1]}')

plot_stats(fit_avg, fit_best, "US State Capital Tour Problem")
plot_route(points, best_ind.gene_list)
