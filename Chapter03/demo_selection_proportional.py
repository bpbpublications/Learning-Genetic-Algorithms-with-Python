import random
import pandas as pd
import matplotlib.pyplot as plt
from ch3.individual import Individual

POPULATION_SIZE = 5
random.seed(1)

unsorted_population = Individual.create_random_population(POPULATION_SIZE)
population = sorted(unsorted_population, key = lambda ind: ind.fitness, reverse = True)
fitness_sum = sum([ind.fitness for ind in population])
fitness_map = {}
for i in population:
    i_prob = round(100 * i.fitness / fitness_sum)
    i_label = f'{i.name} | fitness: {i.fitness}, prob: {i_prob}%'
    fitness_map[i_label] = i.fitness

index = ['Sectors']
df = pd.DataFrame(fitness_map, index = index)
df.plot.barh(stacked = True)
for _ in range(POPULATION_SIZE):
    plt.axvline(x = random.random() * fitness_sum, linewidth = 5, color = 'black')
plt.tick_params(axis = 'x', which = 'both', bottom = False, top = False, labelbottom = False)
plt.show()