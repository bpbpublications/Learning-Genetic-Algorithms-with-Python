import random
import matplotlib.pyplot as plt
from ch9.knapsack.individual import Individual
from ch9.knapsack.random_set_generator import random_set_generator
from ch9.knapsack.toolbox import mutation_bit_flip


def mutate(ind):
    mutated_gene = mutation_bit_flip(ind.gene_list)
    return Individual(mutated_gene)


if __name__ == '__main__':
    random.seed(1)

    random.seed(63)

    items = random_set_generator(1, 100, 0.1, 7, 200)
    Individual.set_items(items)
    Individual.set_max_weight(10)

    gene_set = [0] * len(items)
    inclusions = [2, 30, 34, 42, 48, 64, 85, 104, 113, 119, 157, 174]
    for i in inclusions:
        gene_set[i] = 1
    ind = Individual(gene_set)

    alive = 0
    killed = 0

    for _ in range(1000):
        mutated = mutate(ind)
        if mutated.fitness == 0:
            killed += 1
        else:
            alive += 1

    print(f'Best individual: {ind.fitness}')
    labels = 'Killed', 'Alive'
    sizes = [killed, alive]
    plt.pie(sizes, labels = labels)
    plt.show()