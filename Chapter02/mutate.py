import random
import numpy as np
import matplotlib.pyplot as plt

from ch2.individual import create_random_individual, create_individual
from ch2.fitness import fitness
from ch2.settings import MIN_BORDER, MAX_BORDER


def gene_constraints(g, min_ = MIN_BORDER, max_ = MAX_BORDER):
    if max_ and g > max_:
        g = max_
    if min_ and g < min_:
        g = min_
    return g


def mutate_gaussian(g, mu, sigma):
    mutated_gene = g + random.gauss(mu, sigma)
    return gene_constraints(mutated_gene)


def mutate(ind):
    return create_individual(mutate_gaussian(ind.get_gene(), 0, 1))


if __name__ == '__main__':

    random.seed(37)

    individual = create_random_individual()
    mutated = mutate(individual)

    x = np.linspace(MIN_BORDER, MAX_BORDER)
    plt.plot(x, fitness(x), '--', color = 'blue')
    plt.plot(
        [individual.get_gene()],
        [individual.fitness],
        'o', markersize = 20, color = 'orange'
    )
    plt.plot(
        [mutated.get_gene()],
        [mutated.fitness],
        's', markersize = 20, color = 'green'
    )
    plt.title("Circle : Before Mutation, Square: After Mutation")
    plt.show()
