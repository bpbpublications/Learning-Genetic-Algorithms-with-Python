import random
import pandas as pd
import matplotlib.pyplot as plt
from ch3.individual import Individual

POPULATION_SIZE = 5
random.seed(2)

unsorted_population = Individual.create_random_population(POPULATION_SIZE)
population = sorted(unsorted_population, key = lambda ind: ind.fitness, reverse = True)

fitness_sum = sum([ind.fitness for ind in population])
fitness_map = {}
for i in population:
    i_prob = round(100 * i.fitness / fitness_sum)
    i_label = f'{i.name} | fitness: {i.fitness}, prob: {i_prob}%'
    fitness_map[i_label] = i.fitness

proportional_df = pd.DataFrame(fitness_map, index = ['Sectors'])
proportional_df.plot.barh(stacked = True)
plt.tick_params(axis = 'x', which = 'both', bottom = False, top = False, labelbottom = False)
plt.title('Fitness Proportional Sectors')
plt.show()

rank_step = 1 / POPULATION_SIZE
rank_sum = sum([1 - rank_step * i for i in range(len(population))])
rank_map = {}
for i in range(len(population)):
    i_rank = i + 1
    i_rank_proportion = 1 - i * rank_step
    i_prob = round(100 * i_rank_proportion / rank_sum)
    i_label = f'{population[i].name} | rank: {i_rank}, prob: {i_prob}%'
    rank_map[i_label] = i_rank_proportion

rank_df = pd.DataFrame(rank_map, index = ['Sectors'])
rank_df.plot.barh(stacked = True)
plt.tick_params(axis = 'x', which = 'both', bottom = False, top = False, labelbottom = False)
plt.title('Rank Proportional Sectors')
plt.show()
