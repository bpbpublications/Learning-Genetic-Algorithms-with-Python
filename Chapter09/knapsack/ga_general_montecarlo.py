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

POPULATION_SIZE = 80
CROSSOVER_PROBABILITY = .8
MUTATION_PROBABILITY = .2
MAX_GENERATIONS = 70
RUNS = 100

best = []
total_numbers = []

for _ in range(RUNS):
    first_population = [create_random_individual(len(items), zeros = 30) for _ in range(POPULATION_SIZE)]
    Individual.counter = 0
    best_individual = random.choice(first_population)
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

    best.append(best_individual.fitness)
    total_numbers.append(Individual.counter)

avg_fitness = sum(best) / len(best)
plt.plot(best)
plt.title(f'Average fitness: {avg_fitness} \n'
          f'Average number of individuals: {sum(total_numbers)/ len(total_numbers)}')
plt.axhline(y = avg_fitness, color = 'r', linestyle = '-')
plt.show()
