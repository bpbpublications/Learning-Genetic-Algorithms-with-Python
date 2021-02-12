import random

from ch2.crossover import crossover
from ch2.individual import create_random_individual
from ch2.mutate import mutate
from ch2.population import plot_population
from ch2.selection import select_tournament

if __name__ == '__main__':

    POPULATION_SIZE = 10
    CROSSOVER_PROBABILITY = .8
    MUTATION_PROBABILITY = .1
    MAX_GENERATIONS = 10

    random.seed(29)

    population = [create_random_individual() for _ in range(POPULATION_SIZE)]

    for generation_number in range(POPULATION_SIZE):
        # SELECTION
        selected = select_tournament(population, 3)
        # CROSSOVER
        crossed_offspring = []
        for ind1, ind2 in zip(selected[::2], selected[1::2]):
            if random.random() < CROSSOVER_PROBABILITY:
                children = crossover(ind1, ind2)
                crossed_offspring.append(children[0])
                crossed_offspring.append(children[1])
            else:
                crossed_offspring.append(ind1)
                crossed_offspring.append(ind2)
        # MUTATION
        mutated = []
        for ind in crossed_offspring:
            if random.random() < MUTATION_PROBABILITY:
                mutated.append(mutate(ind))
            else:
                mutated.append(ind)

        population = mutated

        plot_population(population)
