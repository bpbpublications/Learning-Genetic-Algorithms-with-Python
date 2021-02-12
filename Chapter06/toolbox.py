import copy
import random
import matplotlib.pyplot as plt


def constraints(g, min_ = -100, max_ = 100):
    if max_ and g > max_:
        g = max_
    if min_ and g < min_:
        g = min_
    return g


def crossover_blend(p1, p2, alpha):
    c1 = copy.deepcopy(p1)
    c2 = copy.deepcopy(p2)

    for i in range(len(p1)):
        l = min(c1[i], c2[i]) - alpha * abs(c2[i] - c1[i])
        u = max(c1[i], c2[i]) + alpha * abs(c2[i] - c1[i])
        c1[i] = round(l + random.random() * (u - l), 2)
        c2[i] = round(l + random.random() * (u - l), 2)

    return [c1, c2]


def mutation_random_deviation(ind, mu, sigma, p):
    mut = copy.deepcopy(ind)
    for i in range(len(mut)):
        if random.random() < p:
            mut[i] = mut[i] + random.gauss(mu, sigma)
    return mut


def selection_tournament(individuals, group_size = 2):
    selected = []
    for _ in range(len(individuals)):
        candidates = [random.choice(individuals) for _ in range(group_size)]
        selected.append(max(candidates, key = lambda ind: ind.fitness))
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


def stats(population, best_ind, fit_avg, fit_best, fit_best_ever):
    best_of_generation = max(population, key = lambda ind: ind.fitness)
    if best_ind.fitness < best_of_generation.fitness:
        best_ind = best_of_generation
    fit_avg.append(sum([ind.fitness for ind in population]) / len(population))
    fit_best.append(best_of_generation.fitness)
    fit_best_ever.append(max(fit_best + fit_best_ever))

    return best_ind, fit_avg, fit_best, fit_best_ever


def plot_stats(fit_avg, fit_best, fit_best_ever, title):
    plt.plot(fit_avg, label = "Average Fitness of Generation")
    plt.plot(fit_best, label = "Best Fitness of Generation")
    plt.plot(fit_best_ever, label = "Best Fitness Ever")
    plt.title(title)
    plt.legend(loc = "lower right")
    plt.show()
