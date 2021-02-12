import random
from ch9.knapsack.individual import Individual
from ch9.knapsack.toolbox import (
    crossover_one_point, mutation_bit_flip, selection_rank_with_elite,
    get_items_from_my_room,
    crossover_operation,
    mutation_operation,
    stats,
    plot_stats,
)


def crossover(parent1, parent2):
    child1_genes, child2_genes = crossover_one_point(parent1.gene_list, parent2.gene_list)
    return Individual(child1_genes), Individual(child2_genes)


def mutate(ind):
    mutated_gene = mutation_bit_flip(ind.gene_list)
    return Individual(mutated_gene)


Individual.set_items(get_items_from_my_room())
Individual.set_max_weight(10)

random.seed(63)
POPULATION_SIZE = 8
CROSSOVER_PROBABILITY = .7
MUTATION_PROBABILITY = .2
MAX_GENERATIONS = 20

first_population = [Individual.create_random() for _ in range(POPULATION_SIZE)]
population = first_population.copy()
fitness_list = [ind.fitness for ind in population]
fit_avg = [sum(fitness_list) / len(population)]
fit_best = [max(fitness_list)]
fit_best_ever = [max(fitness_list + fit_best)]
best_ind = random.choice(first_population)
population = first_population.copy()

generation_number = 0

while generation_number < MAX_GENERATIONS:
    generation_number += 1
    offspring = selection_rank_with_elite(population, elite_size = 2)
    crossed_offspring = crossover_operation(offspring, crossover, CROSSOVER_PROBABILITY)
    mutated_offspring = mutation_operation(crossed_offspring, mutate, MUTATION_PROBABILITY)
    population = mutated_offspring.copy()

    best_ind, fit_avg, fit_best, fit_best_ever = stats(population, best_ind, fit_avg, fit_best, fit_best_ever)

plot_stats(fit_avg, fit_best_ever, "Knapsack Problem")
best_ind.plot_info()
