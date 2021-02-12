import copy
import random
import matplotlib.pyplot as plt


def crossover_blend(p1, p2, alpha):
    c1 = copy.deepcopy(p1)
    c2 = copy.deepcopy(p2)

    l = min(c1, c2) - alpha * abs(c2 - c1)
    u = max(c1, c2) + alpha * abs(c2 - c1)
    c1 = l + random.random() * (u - l)
    c2 = l + random.random() * (u - l)

    return [c1, c2]


def mutation_random_deviation(ind, mu, sigma, p):
    mut = copy.deepcopy(ind)
    if random.random() < p:
        mut = mut + random.gauss(mu, sigma)
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


def plot_stats(fit_avg, fit_best, fit_best_ever, title):
    plt.plot(fit_avg, label = "Average Fitness of Gen")
    plt.plot(fit_best, label = "Best Fitness of Gen")
    plt.plot(fit_best_ever, label = "Best Fitness")
    plt.title(title)
    plt.legend(loc = "lower right")
    plt.show()


def stats(population, best_ind, fit_avg, fit_best, fit_best_ever):
    best_of_generation = max(population, key = lambda ind: ind.fitness)
    if best_ind.fitness < best_of_generation.fitness:
        best_ind = best_of_generation
    fit_avg.append(sum([ind.fitness for ind in population]) / len(population))
    fit_best.append(best_of_generation.fitness)
    fit_best_ever.append(max(fit_best + fit_best_ever))

    return best_ind, fit_avg, fit_best, fit_best_ever
