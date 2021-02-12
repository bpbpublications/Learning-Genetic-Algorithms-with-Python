import copy
import random

import matplotlib.pyplot as plt
from math import nan, copysign

from ch10.tsp.individual import Individual


def selection_rank_with_elite(individuals, elite_size = 0):
    sorted_individuals = sorted(individuals, key = lambda ind: ind.fitness, reverse = True)
    rank_distance = 1 / len(individuals)
    ranks = [(1 - i * rank_distance) for i in range(len(individuals))]
    ranks_sum = sum(ranks)
    selected = sorted_individuals[0:elite_size]

    for i in range(len(sorted_individuals) - elite_size):
        shave = random.random() * ranks_sum
        rank_sum = 0
        for i in range(len(sorted_individuals)):
            rank_sum += ranks[i]
            if rank_sum > shave:
                selected.append(sorted_individuals[i])
                break

    return selected


def crossover_fitness_driven_order(ind1, ind2):
    p1, p2 = ind1.gene_list, ind2.gene_list
    zero_shift = min(p1)
    length = len(p1)
    start, end = sorted([random.randrange(length) for _ in range(2)])
    c1, c2 = [nan] * length, [nan] * length
    t1, t2 = [x - zero_shift for x in p1], [x - zero_shift for x in p2]

    spaces1, spaces2 = [True] * length, [True] * length
    for i in range(length):
        if i < start or i > end:
            spaces1[t2[i]] = False
            spaces2[t1[i]] = False

    j1, j2 = end + 1, end + 1
    for i in range(length):
        if not spaces1[t1[(end + i + 1) % length]]:
            c1[j1 % length] = t1[(end + i + 1) % length]
            j1 += 1

        if not spaces2[t2[(i + end + 1) % length]]:
            c2[j2 % length] = t2[(i + end + 1) % length]
            j2 += 1

    for i in range(start, end + 1):
        c1[i], c2[i] = t2[i], t1[i]

    child1 = Individual([x + zero_shift for x in c1])
    child2 = Individual([x + zero_shift for x in c2])

    candidates = [child1, child2, ind1, ind2]
    best = sorted(candidates, key = lambda ind: ind.fitness, reverse = True)

    return best[0:2]


def mutation_fitness_driven_shift(ind, max_tries = 3):
    for t in range(0, max_tries):
        mut = copy.deepcopy(ind.gene_list)
        pos = random.sample(range(0, len(mut)), 2)
        g1 = mut[pos[0]]
        dir = int(copysign(1, pos[1] - pos[0]))
        for i in range(pos[0], pos[1], dir):
            mut[i] = mut[i + dir]
        mut[pos[1]] = g1
        mutated = Individual(mut)
        if mutated.fitness > ind.fitness:
            return mutated
    return ind


def crossover_operation(population, method, prob):
    crossed_offspring = []
    for ind1, ind2 in zip(population[::2], population[1::2]):
        if random.random() < prob:
            kid1, kid2 = method(ind1, ind2)
            crossed_offspring.append(kid1)
            crossed_offspring.append(kid2)
        else:
            crossed_offspring.append(ind1)
            crossed_offspring.append(ind2)
    return crossed_offspring


def mutation_operation(population, method, prob):
    mutated_offspring = []
    for mutant in population:
        if random.random() < prob:
            new_mutant = method(mutant)
            mutated_offspring.append(new_mutant)
        else:
            mutated_offspring.append(mutant)
    return mutated_offspring


def stats(population, best_ind, fit_avg, fit_best):
    best_of_generation = max(population, key = lambda ind: ind.fitness)
    if best_ind.fitness < best_of_generation.fitness:
        best_ind = best_of_generation
    fit_avg.append(sum([ind.fitness for ind in population]) / len(population))
    fit_best.append(best_ind.fitness)

    return best_ind, fit_avg, fit_best


def plot_stats(fit_avg, fit_best, title):
    plt.plot(fit_avg, label = "Average Fitness of Generation")
    plt.plot(fit_best, label = "Best Fitness")
    plt.title(title)
    plt.legend(loc = "lower right")
    plt.show()
