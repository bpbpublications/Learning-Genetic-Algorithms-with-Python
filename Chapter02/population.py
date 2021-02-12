import random
import numpy as np
import matplotlib.pyplot as plt

from ch2.individual import create_random_individual
from ch2.fitness import fitness
from ch2.settings import MIN_BORDER, MAX_BORDER


def get_best_individual(population):
    return max(population, key = lambda ind: ind.fitness)


def get_average_fitness(population):
    return sum([i.fitness for i in population]) / len(population)


def plot_population(population):
    best_ind = get_best_individual(population)
    best_fitness = best_ind.fitness
    average_fitness = get_average_fitness(population)

    x = np.linspace(MIN_BORDER, MAX_BORDER)
    plt.plot(x, fitness(x), '--', color = 'blue')
    plt.plot(
        [ind.get_gene() for ind in population],
        [ind.fitness for ind in population],
        'o', color = 'orange'
    )
    plt.plot(
        [best_ind.get_gene()], [best_ind.fitness],
        's', color = 'green')
    plt.plot(
        [MIN_BORDER, MAX_BORDER],
        [average_fitness, average_fitness],
        color = 'grey'
    )
    plt.title(f"Best Individual: {best_ind}, Best Fitness: {best_fitness:.2f} \n "
              f"Average Population Fitness: {average_fitness:.2f}"
              )
    plt.show()


if __name__ == '__main__':

    POPULATION_SIZE = 10

    random.seed(22)

    population = [create_random_individual() for _ in range(POPULATION_SIZE)]
    plot_population(population)
