import copy
import random
from ch9.radar.individual import Individual
from ch9.radar.landscape import SquareType, Square, generate_random_landscape, plot_coverage
from ch9.radar.toolbox import (
    selection_rank_with_elite,
    crossover_operation,
    mutation_operation,
    plot_stats,
    stats,
    crossover_n_point,
    mutation_bit_flip,
)


def crossover(parent1, parent2):
    child1_genes, child2_genes = crossover_n_point(parent1.gene_list, parent2.gene_list, 3)
    return Individual(child1_genes), Individual(child2_genes)


def mutate(ind):
    mut = mutation_bit_flip(ind.gene_list)
    return Individual(mut)


def select(population):
    return selection_rank_with_elite(population, elite_size = 2)


random.seed(15)

rows = 60
cols = 60
radar_radius = 7

square_grid = {
    Square(SquareType.water, needs_coverage = False, tower_cost = 500): 20,
    Square(SquareType.land, needs_coverage = False, tower_cost = 30):   100,
    Square(SquareType.hill, needs_coverage = False, tower_cost = 100):  8,
    Square(SquareType.city, needs_coverage = True, tower_cost = 200):   1
}

landscape = generate_random_landscape(list(square_grid.keys()), square_grid, rows, cols)


def fitness_function(coords):
    global landscape, radar_radius
    test_landscape = copy.deepcopy(landscape)
    test_landscape.add_radars(coords, radar_radius)
    return - test_landscape.uncovered_count() * 500 - test_landscape.radar_cost()


Individual.rows = rows
Individual.cols = cols
Individual.set_fitness_function(fitness_function)

POPULATION_SIZE = 60
CROSSOVER_PROBABILITY = .5
MUTATION_PROBABILITY = .5
MAX_GENERATIONS = 400

first_population = [Individual.generate_random(.005) for _ in range(POPULATION_SIZE)]
best_ind = random.choice(first_population)
fit_avg = []
fit_best = []
generation_num = 0
population = first_population.copy()
generation_number = 0

while generation_num < MAX_GENERATIONS:
    generation_num += 1
    offspring = selection_rank_with_elite(population, elite_size = 2)
    crossed_offspring = crossover_operation(offspring, crossover, CROSSOVER_PROBABILITY)
    mutated_offspring = mutation_operation(crossed_offspring, mutate, MUTATION_PROBABILITY)
    population = mutated_offspring.copy()
    best_ind, fit_avg, fit_best = stats(population, best_ind, fit_avg, fit_best)
    print(f'Generation {generation_num}. Avg fit: {fit_avg[-1]}. Best fit: {best_ind.fitness}')

    test_landscape = copy.deepcopy(landscape)
    test_landscape.add_radars(best_ind.get_coordinates(), radar_radius)
    plot_coverage(test_landscape, title = f"Best Individual for Generation: {generation_num}")

plot_stats(fit_avg, fit_best, "Radar Placement Problem")

plot_coverage(landscape, title = "Cities")
landscape.add_radars(best_ind.get_coordinates(), radar_radius)
plot_coverage(landscape, title = "Best Radar Placement")

print(f'Radar Count: {best_ind.count_radars()}')
print(f'Best Fitness: {best_ind.fitness}')
