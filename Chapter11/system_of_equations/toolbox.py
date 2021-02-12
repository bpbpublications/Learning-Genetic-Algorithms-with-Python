import copy
import random


def constraints(g, min_ = -10_000, max_ = 10_000):
    if max_ and g > max_:
        g = max_
    if min_ and g < min_:
        g = min_
    return round(g)


def crossover_blend(p1, p2, alpha):
    c1 = copy.deepcopy(p1)
    c2 = copy.deepcopy(p2)

    for i in range(len(p1)):
        l = min(c1[i], c2[i]) - alpha * abs(c2[i] - c1[i])
        u = max(c1[i], c2[i]) + alpha * abs(c2[i] - c1[i])
        c1[i] = l + random.random() * (u - l)
        c2[i] = l + random.random() * (u - l)

    return [c1, c2]


def mutation_random_deviation(ind, mu, sigma, p):
    mut = copy.deepcopy(ind)
    for i in range(len(mut)):
        if random.random() < p:
            mut[i] = mut[i] + random.gauss(mu, sigma)
    return mut


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
