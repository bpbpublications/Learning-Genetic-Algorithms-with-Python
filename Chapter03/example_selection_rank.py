import random

from ch3.selection_rank import selection_rank
from ch3.individual import Individual

POPULATION_SIZE = 5
random.seed(18)

population = Individual.create_random_population(POPULATION_SIZE)
selected = selection_rank(population)

print(f'Population: {population}')
print(f'Selected: {selected}')
