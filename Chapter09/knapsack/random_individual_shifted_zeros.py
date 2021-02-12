import random

from ch9.knapsack.individual import Individual
from ch9.knapsack.random_set_generator import random_set_generator


def create_random_individual(gene_len, zeros = 1, ones = 1):
    s = ([0] * zeros) + ([1] * ones)
    return Individual([random.choice(s) for _ in range(gene_len)])


if __name__ == '__main__':
    random.seed(1)

    items = random_set_generator(1, 100, 0.1, 7, 200)
    Individual.set_items(items)
    Individual.set_max_weight(10)

    population = [create_random_individual(len(items), 50, 1) for _ in range(1000)]
    average_weight = sum([ind.total_weight() for ind in population]) / len(population)
    print(f'Average weight of population: {average_weight}')
