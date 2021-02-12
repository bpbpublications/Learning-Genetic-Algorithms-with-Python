import random


def selection_stochastic_universal_sampling(individuals):
    sorted_individuals = sorted(individuals, key = lambda ind: ind.fitness, reverse = True)
    fitness_sum = sum([ind.fitness for ind in individuals])

    distance = fitness_sum / len(individuals)
    shift = random.uniform(0, distance)
    borders = [shift + i * distance for i in range(len(individuals))]

    selected = []
    for border in borders:
        i = 0
        roulette_sum = sorted_individuals[i].fitness
        while roulette_sum < border:
            i += 1
            roulette_sum += sorted_individuals[i].fitness
        selected.append(sorted_individuals[i])

    return selected
