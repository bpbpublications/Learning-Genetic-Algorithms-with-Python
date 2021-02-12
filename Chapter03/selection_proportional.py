import random

def selection_proportional(individuals):
    sorted_individuals = sorted(individuals, key = lambda ind: ind.fitness, reverse = True)
    fitness_sum = sum([ind.fitness for ind in individuals])
    selected = []

    for _ in range(len(sorted_individuals)):
        shave = random.random() * fitness_sum
        roulette_sum = 0
        for ind in sorted_individuals:
            roulette_sum += ind.fitness
            if roulette_sum > shave:
                selected.append(ind)
                break

    return selected
