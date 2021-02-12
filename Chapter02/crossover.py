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


def crossover_blend(g1, g2, alpha = 0.3):
    shift = (1. + 2. * alpha) * random.random() - alpha
    new_g1 = (1. - shift) * g1 + shift * g2
    new_g2 = shift * g1 + (1. - shift) * g2

    return gene_constraints(new_g1), gene_constraints(new_g2)


def crossover(ind1, ind2):
    offspring_genes = crossover_blend(ind1.get_gene(), ind2.get_gene())
    return [create_individual(offspring_genes[0]),
            create_individual(offspring_genes[1])]


if __name__ == '__main__':
    random.seed(30)

    p_1 = create_random_individual()
    p_2 = create_random_individual()

    offspring = crossover(p_1, p_2)

    c_1 = offspring[0]
    c_2 = offspring[1]

    x = np.linspace(MIN_BORDER, MAX_BORDER)
    plt.plot(x, fitness(x), '--', color = 'blue')
    plt.plot(
        [p_1.get_gene(), p_2.get_gene()],
        [p_1.fitness, p_2.fitness],
        'o', markersize = 15, color = 'orange'
    )
    plt.plot(
        [c_1.get_gene(), c_2.get_gene()],
        [c_1.fitness, c_2.fitness],
        's', markersize = 15, color = 'green'
    )
    plt.title("Circle : Parents, Square: Children")
    plt.show()
