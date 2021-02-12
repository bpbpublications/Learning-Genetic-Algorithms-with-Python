import random
import matplotlib.pyplot as plt
from ch10.tsp.individual import Individual, generate_random
from ch10.tsp.route import get_us_capitals
from ch10.tsp.toolbox import (
    crossover_fitness_driven_order, mutation_fitness_driven_shift, selection_rank_with_elite,
    crossover_operation,
    stats,
    mutation_operation,
    mutation_fitness_driven_shuffle,
)


def crossover(parent1, parent2):
    return crossover_fitness_driven_order(parent1, parent2)


def mutate_shift(ind):
    return mutation_fitness_driven_shift(ind)


def mutate_shuffle(ind):
    return mutation_fitness_driven_shuffle(ind)


def select(population):
    return selection_rank_with_elite(population, elite_size = 2)


points = get_us_capitals()
Individual.points = points

random.seed(60)

RUNS = 100
TEST_PARAMETERS = {
    'Shuffle Mutation': mutation_fitness_driven_shuffle,
    'Shift Mutation':   mutation_fitness_driven_shift
}
CROSSOVER_PROBABILITY = .3
MUTATION_PROBABILITY = .9
POPULATION_SIZE = 200
MAX_GENERATIONS = 200

results = [None] * len(TEST_PARAMETERS)
counter = [None] * len(TEST_PARAMETERS)

for design in range(len(TEST_PARAMETERS)):

    results[design] = []
    counter[design] = []

    mutate = list(TEST_PARAMETERS.values())[design]

    print(f'Testing : {list(TEST_PARAMETERS.keys())[design]}')

    for r in range(RUNS):
        Individual.count = 0
        first_population = [generate_random(len(points)) for _ in range(POPULATION_SIZE)]
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

        results[design].append(fit_best[-1])
        counter[design].append(Individual.count)

        print(f'Best Individual: {fit_best[-1]} for run: {r}')

plt.boxplot([results[0], results[1]])
plt.title("Best Individual Distribution \n Shuffle Mutation VS Shift Mutation")
plt.xticks(range(1, len(TEST_PARAMETERS) + 1), TEST_PARAMETERS.keys())
plt.show()

plt.boxplot([counter[0], counter[1]])
plt.title("Total Number of Individuals Distribution \n Shuffle Mutation VS Shift Mutation")
plt.xticks(range(1, len(TEST_PARAMETERS) + 1), TEST_PARAMETERS.keys())
plt.show()
