import random
import matplotlib.pyplot as plt
from numpy import mean

from ch10.tsp.individual import Individual, generate_random
from ch10.tsp.route import get_us_capitals
from ch12.toolbox import (
    selection_rank_with_elite,
    crossover_operation,
    stats,
    mutation_operation,
    crossover_fitness_driven_order,
    mutation_fitness_driven_shift,
)
from ch12.learning_rate import average, is_learning_positive


def crossover(parent1, parent2):
    return crossover_fitness_driven_order(parent1, parent2)


def mutate(ind):
    return mutation_fitness_driven_shift(ind)


points = get_us_capitals()
Individual.points = points

random.seed(3)


def adaptive_genetic_algorithm():
    POPULATION_SIZE = 200
    MIN_POPULATION_SIZE = 50
    MAX_POPULATION_SIZE = 300

    CROSSOVER_PROBABILITY = .5
    MIN_CROSSOVER_PROBABILITY = .1

    MUTATION_PROBABILITY = .5
    MIN_MUTATION_PROBABILITY = .1

    MAX_GENERATIONS = 10_000
    MIN_GENERATIONS = 100

    ELITE_SIZE = 1

    Individual.count = 0
    first_population = [generate_random(len(points)) for _ in range(POPULATION_SIZE)]
    best_ind = random.choice(first_population)
    fit_avg = []
    fit_best = []
    learn_trend = []
    ev_avg = []
    population_size = []
    mutation_prob = []
    crossover_prob = []
    generation_num = 0
    population = first_population.copy()

    while generation_num < MIN_GENERATIONS or\
            (generation_num < MAX_GENERATIONS and is_learning_positive(fit_best, 50, .001)):
        generation_num += 1
        offspring = selection_rank_with_elite(population, elite_size = ELITE_SIZE)
        crossed_offspring = crossover_operation(offspring, crossover, CROSSOVER_PROBABILITY)
        mutated_offspring = mutation_operation(crossed_offspring, mutate, MUTATION_PROBABILITY)
        population = mutated_offspring.copy()
        best_ind, fit_avg, fit_best = stats(population, best_ind, fit_avg, fit_best)
        ev_avg.append(average(fit_avg, 10))
        learn_rate = is_learning_positive(fit_avg, 10, .001)
        learn_trend.append(learn_rate)
        if not learn_rate:
            MUTATION_PROBABILITY = min(MUTATION_PROBABILITY * 1.1, 1)
            CROSSOVER_PROBABILITY = min(CROSSOVER_PROBABILITY * 1.1, 1)
            if len(population) < MAX_POPULATION_SIZE:
                population = population + [generate_random(len(points)) for _ in range(2)]
        else:
            MUTATION_PROBABILITY = max(MUTATION_PROBABILITY * .99, MIN_MUTATION_PROBABILITY)
            CROSSOVER_PROBABILITY = max(CROSSOVER_PROBABILITY * .99, MIN_CROSSOVER_PROBABILITY)
            if len(population) > MIN_POPULATION_SIZE:
                worst_ind = min(population, key = lambda ind: ind.fitness)
                population.remove(worst_ind)

        population_size.append(len(population))
        crossover_prob.append(CROSSOVER_PROBABILITY)
        mutation_prob.append(MUTATION_PROBABILITY)

    return best_ind.fitness, Individual.count


def classical_genetic_algorithm():
    POPULATION_SIZE = 140
    CROSSOVER_PROBABILITY = .3
    MUTATION_PROBABILITY = .9
    MAX_GENERATIONS = 140

    Individual.count = 0
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

    return best_ind.fitness, Individual.count


RUNS = 100
adaptive_results = []
adaptive_total_ind_list = []
classical_results = []
classical_total_ind_list = []
for i in range(1, RUNS + 1):
    print(f'run - {i}')
    adaptive_result, adaptive_total_ind = adaptive_genetic_algorithm()
    classical_result, classical_total_ind = classical_genetic_algorithm()
    adaptive_results.append(adaptive_result)
    adaptive_total_ind_list.append(adaptive_total_ind)
    classical_results.append(classical_result)
    classical_total_ind_list.append(classical_total_ind)
    print(f'Adaptive: {mean(adaptive_results)}')
    print(f'Classical: {mean(classical_results)}')

plt.boxplot([adaptive_results, classical_results])
plt.title("Adaptive Genetic Algorithm vs Classical Genetic Algorithm "
          "\n Best Fitness:")
plt.xticks([0, 1, 2], ["", "Adaptive", "Classical"])
plt.show()

plt.boxplot([adaptive_total_ind_list, classical_total_ind_list])
plt.title("Adaptive Genetic Algorithm vs Classical Genetic Algorithm "
          "\n Total Number of Individuals in Evolution:")
plt.xticks([0, 1, 2], ["", "Adaptive", "Classical"])
plt.show()
