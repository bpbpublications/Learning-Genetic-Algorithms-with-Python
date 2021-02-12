import random
import pandas as pd
import matplotlib.pyplot as plt

from ch3.individual import Individual

POPULATION_SIZE = 10
TOURNAMENT_SIZE = 3

random.seed(7)

population = Individual.create_random_population(POPULATION_SIZE)
candidates = [random.choice(population) for _ in range(TOURNAMENT_SIZE)]
best = [max(candidates, key = lambda ind: ind.fitness)]


def plot_individuals(individual_set):
    df = pd.DataFrame({
        'name':    [ind.name for ind in individual_set],
        'fitness': [ind.fitness for ind in individual_set]
    })
    df.plot.bar(x = 'name', y = 'fitness', rot = 0)
    plt.show()


plot_individuals(population)
plot_individuals(candidates)
plot_individuals(best)
