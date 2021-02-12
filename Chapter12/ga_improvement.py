import random
import matplotlib.pyplot as plt
from ch10.tsp.individual import Individual, generate_random
from ch10.tsp.route import get_us_capitals
from ch12.evolution_stats import average, is_improvement_positive
from ch12.toolbox import (
    selection_rank_with_elite,
    crossover_operation,
    stats,
    mutation_operation,
    crossover_fitness_driven_order,
    mutation_fitness_driven_shift,
)


def crossover(parent1, parent2):
    return crossover_fitness_driven_order(parent1, parent2)


def mutate(ind):
    return mutation_fitness_driven_shift(ind)


points = get_us_capitals()
Individual.points = points

random.seed(1)

POPULATION_SIZE = 300

CROSSOVER_PROBABILITY = .5
MUTATION_PROBABILITY = .5
MAX_GENERATIONS = 150

ELITE_SIZE = 2

first_population = [generate_random(len(points)) for _ in range(POPULATION_SIZE)]
best_ind = random.choice(first_population)
fit_avg = []
fit_best = []
impr_list = []
ev_avg = []
generation_num = 0
population = first_population.copy()

while generation_num < MAX_GENERATIONS:
    generation_num += 1
    offspring = selection_rank_with_elite(population, elite_size = ELITE_SIZE)
    crossed_offspring = crossover_operation(offspring, crossover, CROSSOVER_PROBABILITY)
    mutated_offspring = mutation_operation(crossed_offspring, mutate, MUTATION_PROBABILITY)
    population = mutated_offspring.copy()
    best_ind, fit_avg, fit_best = stats(population, best_ind, fit_avg, fit_best)
    ev_avg.append(average(fit_avg, 10))
    impr_list.append(is_improvement_positive(fit_avg, 10, .001))


def add_degradation_areas(learn_trend):
    for i in range(len(learn_trend)):
        if not learn_trend[i]:
            plt.axvspan(i, i + 1, color = 'red', alpha = 0.1)


plt.plot(ev_avg[100:], label = "Average Fitness of Evolution")
plt.plot(fit_avg[100:], label = "Average Fitness of Generation")
plt.xticks([])
add_degradation_areas(impr_list[100:])
plt.legend(loc = "lower right")
plt.title("Genetic Algorithm Progress \n"
          "Starting from 100th Generation")
plt.show()
