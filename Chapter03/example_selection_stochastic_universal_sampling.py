import random

from ch3.selection_stochastic_universal_sampling import selection_stochastic_universal_sampling
from ch3.individual import Individual

POPULATION_SIZE = 5
random.seed(4)

population = Individual.create_random_population(POPULATION_SIZE)
selected = selection_stochastic_universal_sampling(population)

print("Population:")
[print(ind) for ind in population]

print("Selected:")
[print(ind) for ind in selected]
