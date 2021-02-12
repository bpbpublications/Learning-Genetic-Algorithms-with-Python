import copy
import random


def closest(value, value_list):
    return min(value_list, key = lambda x: abs(x - value))


def mutation_random_uniform_deviation(ind):
    mut = copy.deepcopy(ind)
    for i in range(len(mut)):
        mut[i] = mut[i] + random.uniform(-1, 1)
    return mut


class DiscreteIndividual:
    x_set = range(-1000, 1001, 2)

    def __init__(self, gene_list):
        self.gene_list = [closest(gene_list[0], self.x_set)]


class RealIndividual:

    def __init__(self, gene_list):
        self.gene_list = gene_list


if __name__ == '__main__':

    random.seed(5)

    disc_ind = DiscreteIndividual([0])
    real_ind = RealIndividual([0])

    for _ in range(0, 1000):
        real_ind = RealIndividual(mutation_random_uniform_deviation(real_ind.gene_list))
        disc_ind = DiscreteIndividual(mutation_random_uniform_deviation(disc_ind.gene_list))

    print(f'Discrete Individual: {disc_ind.gene_list}')
    print(f'Real Individual: {real_ind.gene_list}')
