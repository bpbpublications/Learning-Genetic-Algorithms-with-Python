import random

from ch11.graph.graph_utils import plot_graph, get_edges, get_vertices_from_edges
from ch11.graph.individual import Individual
from ch11.graph.toolbox import (
    crossover_fitness_driven_n_point, mutation_fitness_driven_random_change,
    selection_rank_with_elite,
    crossover_operation,
    mutation_operation,
)


def crossover(parent1, parent2):
    return crossover_fitness_driven_n_point(parent1, parent2, 2)


def mutate(ind):
    return mutation_fitness_driven_random_change(ind, range(3), 3)


def select(population):
    return selection_rank_with_elite(population, elite_size = 2)


random.seed(1)

edges = get_edges()
Individual.vertex_number = len(get_vertices_from_edges(edges))
Individual.edges = edges

random.seed(7)
POPULATION_SIZE = 500
CROSSOVER_PROBABILITY = .5
MUTATION_PROBABILITY = .5
MAX_GENERATIONS = 200

first_population = [Individual.generate_random() for _ in range(POPULATION_SIZE)]
best_ind = random.choice(first_population)
generation_number = 0

population = first_population.copy()

while generation_number < MAX_GENERATIONS and best_ind.fitness != 0:
    generation_number += 1
    offspring = select(population)
    crossed_offspring = crossover_operation(offspring, crossover, CROSSOVER_PROBABILITY)
    mutated_offspring = mutation_operation(crossed_offspring, mutate, MUTATION_PROBABILITY)
    population = mutated_offspring.copy()

    best_of_generation = max(population, key = lambda ind: ind.fitness)
    if best_ind.fitness < best_of_generation.fitness:
        best_ind = best_of_generation
    print(f'Generation: {generation_number}, best fit: {best_ind.fitness}')

print(f'Best Individual Fitness: {best_ind.fitness}')
plot_graph(edges, best_ind.vertex_colors())
