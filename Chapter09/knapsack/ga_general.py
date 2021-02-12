import random
import matplotlib.pyplot as plt
from ch9.knapsack.individual import Individual
from ch9.knapsack.random_individual_shifted_zeros import create_random_individual
from ch9.knapsack.random_set_generator import random_set_generator
from ch9.knapsack.toolbox import (
    crossover_one_point, mutation_bit_flip, selection_rank_with_elite,
)


def crossover(parent1, parent2):
    child1_genes, child2_genes = crossover_one_point(parent1.gene_list, parent2.gene_list)
    return Individual(child1_genes), Individual(child2_genes)


def mutate(ind):
    mutated_gene = mutation_bit_flip(ind.gene_list)
    return Individual(mutated_gene)


def select(population):
    return selection_rank_with_elite(population, elite_size = 2)


random.seed(63)

items = random_set_generator(1, 100, 0.1, 7, 200)
Individual.set_items(items)
Individual.set_max_weight(10)

POPULATION_SIZE = 100
CROSSOVER_PROBABILITY = .7
MUTATION_PROBABILITY = .2
MAX_GENERATIONS = 100

first_population = [create_random_individual(len(items), zeros = 30) for _ in range(POPULATION_SIZE)]
best_individual = random.choice(first_population)
stats_fitness_average = []
stats_fitness_best = []
generation_number = 0

population = first_population.copy()

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

    best_of_generation = max(population, key = lambda ind: ind.fitness)
    if best_individual.fitness < best_of_generation.fitness:
        best_individual = best_of_generation
    stats_fitness_average.append(sum([ind.fitness for ind in population]) / len(population))
    stats_fitness_best.append(best_individual.fitness)

plt.plot(stats_fitness_average, label = "Average Fitness of Generation")
plt.plot(stats_fitness_best, label = "Best Fitness")
plt.title("General Knapsack Problem")
plt.legend(loc = "lower right")
plt.show()

print(f'Best Fitness: {best_individual.fitness}')
print(f'Total Number of Individuals: {Individual.counter}')
