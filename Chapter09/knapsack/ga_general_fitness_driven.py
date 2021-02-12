import random
from ch9.knapsack.individual import Individual
from ch9.knapsack.random_individual_shifted_zeros import create_random_individual
from ch9.knapsack.random_set_generator import random_set_generator
from ch9.knapsack.toolbox import (
    selection_rank_with_elite, crossover_fitness_driven_one_point,
    mutation_fitness_driven_bit_flip,
    plot_stats,
    stats,
    crossover_operation,
    mutation_operation,
)


def crossover(parent1, parent2):
    return crossover_fitness_driven_one_point(parent1, parent2)


def mutate(ind):
    return mutation_fitness_driven_bit_flip(ind, max_tries = 3)


def select(population):
    return selection_rank_with_elite(population, elite_size = 2)


random.seed(68)
items = random_set_generator(1, 100, 0.1, 7, 200)
Individual.set_items(items)
Individual.set_max_weight(10)

POPULATION_SIZE = 100
CROSSOVER_PROBABILITY = .7
MUTATION_PROBABILITY = .2
MAX_GENERATIONS = 50

first_population = [create_random_individual(len(items), zeros = 30) for _ in range(POPULATION_SIZE)]
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

plot_stats(fit_avg, fit_best_ever, "General Knapsack Problem")
print(f'Best Fitness: {best_ind.fitness}')
print(f'Total Number of Individuals: {Individual.counter}')
