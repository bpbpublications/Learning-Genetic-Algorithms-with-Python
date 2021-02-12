import random
import matplotlib.pyplot as plt
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
from ch12.evolution_stats import average, is_improvement_positive


def crossover(parent1, parent2):
    return crossover_fitness_driven_order(parent1, parent2)


def mutate(ind):
    return mutation_fitness_driven_shift(ind)


def selection(population):
    return selection_rank_with_elite(population, elite_size = 1)


points = get_us_capitals()
Individual.points = points

random.seed(194)

POPULATION_SIZE = 200
MIN_POPULATION_SIZE = 50
MAX_POPULATION_SIZE = 300

CROSSOVER_PROBABILITY = .5
MIN_CROSSOVER_PROBABILITY = .1

MUTATION_PROBABILITY = .5
MIN_MUTATION_PROBABILITY = .1

MAX_GENERATIONS = 10_000
MIN_GENERATIONS = 100

fit_avg = []
fit_best = []
impr_list = []
ev_avg = []
population_size = []
mutation_prob = []
crossover_prob = []
generation_num = 0
first_population = [generate_random(len(points))
                    for _ in range(POPULATION_SIZE)]
best_ind = random.choice(first_population)
population = first_population.copy()

while generation_num < MIN_GENERATIONS or\
        (generation_num < MAX_GENERATIONS and
         is_improvement_positive(fit_best, 50, .001)):

    generation_num += 1
    offspring = selection(population)
    crossed_offspring = crossover_operation(offspring, crossover, CROSSOVER_PROBABILITY)
    mutated_offspring = mutation_operation(crossed_offspring, mutate, MUTATION_PROBABILITY)
    population = mutated_offspring.copy()
    best_ind, fit_avg, fit_best = stats(population, best_ind, fit_avg, fit_best)
    ev_avg.append(average(fit_avg, 10))
    impr_rate = is_improvement_positive(fit_avg, 10, .001)
    impr_list.append(impr_rate)
    if not impr_rate:
        MUTATION_PROBABILITY = min(MUTATION_PROBABILITY * 1.1, 1)
        CROSSOVER_PROBABILITY = min(CROSSOVER_PROBABILITY * 1.1, 1)
        if len(population) < MAX_POPULATION_SIZE:
            population = population + \
                         [generate_random(len(points)) for _ in range(2)]
    else:
        MUTATION_PROBABILITY = max(MUTATION_PROBABILITY * .99, MIN_MUTATION_PROBABILITY)
        CROSSOVER_PROBABILITY = max(CROSSOVER_PROBABILITY * .99, MIN_CROSSOVER_PROBABILITY)
        if len(population) > MIN_POPULATION_SIZE:
            worst_ind = min(population, key = lambda ind: ind.fitness)
            population.remove(worst_ind)

    population_size.append(len(population))
    crossover_prob.append(CROSSOVER_PROBABILITY)
    mutation_prob.append(MUTATION_PROBABILITY)

print(best_ind.fitness)


def add_degradation_areas(learn_trend):
    for i in range(len(learn_trend)):
        if not learn_trend[i]:
            plt.axvspan(i, i + 1, color = 'red', alpha = 0.1)


# Plot Progress
plt.plot(ev_avg, label = "Average Fitness of Evolution")
plt.plot(fit_avg, label = "Average Fitness of Generation")
plt.plot(fit_best, label = "Best Fitness")
add_degradation_areas(impr_list)
plt.legend(loc = "lower right")
plt.title(f"Adaptive Genetic Algorithm Progress \n"
          f"Best Individual: {best_ind.fitness} \n"
          f"Total Number of Individuals: {Individual.count} \n"
          f"Number of Generations: {generation_num}")
plt.show()

# Evolution Population Size Progress
plt.plot(population_size)
add_degradation_areas(impr_list)
plt.title("Evolution Population Size Progress")
plt.show()

# Crossover Probability Progress
plt.plot(crossover_prob)
add_degradation_areas(impr_list)
plt.title("Crossover Probability Progress")
plt.show()

# Mutation Probability Progress
plt.plot(mutation_prob)
add_degradation_areas(impr_list)
plt.title("Mutation Probability Progress")
plt.show()
