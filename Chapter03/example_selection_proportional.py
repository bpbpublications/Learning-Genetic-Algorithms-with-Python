import random
from ch3.selection_proportional import selection_proportional
from ch3.individual import Individual

POPULATION_SIZE = 5
random.seed(4)

population = Individual.create_random_population(POPULATION_SIZE)
selected = selection_proportional(population)

print(f"Population: {population}")
print(f"Selected: {selected}")
