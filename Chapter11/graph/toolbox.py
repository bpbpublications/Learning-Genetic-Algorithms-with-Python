import copy
import random

import matplotlib.pyplot as plt

from ch11.graph.individual import Individual


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


def crossover_fitness_driven_n_point(ind1, ind2, n):
    p1, p2 = ind1.gene_list, ind2.gene_list
    ps = random.sample(range(1, len(p1) - 1), n)
    ps.append(0)
    ps.append(len(p1))
    ps = sorted(ps)
    c1, c2 = copy.deepcopy(p1), copy.deepcopy(p2)
    for i in range(0, n + 1):
        if i % 2 == 0:
            continue
        c1[ps[i]:ps[i + 1]] = p2[ps[i]:ps[i + 1]]
        c2[ps[i]:ps[i + 1]] = p1[ps[i]:ps[i + 1]]

    child1 = Individual(c1)
    child2 = Individual(c2)

    candidates = [child1, child2, ind1, ind2]
    best = sorted(candidates, key = lambda ind: ind.fitness, reverse = True)

    return best[0:2]


def mutation_fitness_driven_random_change(ind, values_set, max_tries = 3):
    for _ in range(0, max_tries):
        mut = copy.deepcopy(ind.gene_list)
        pos = random.choice(range(0, len(mut)))
        mut[pos] = random.choice(values_set)
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
