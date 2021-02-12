import random
from ch8.toolbox import crossover_blend, mutation_random_deviation


def closest(value, value_list):
    return min(value_list, key = lambda x: abs(x - value))


class Individual:
    x_set = range(-10, 11)
    y_set = range(0, 1000, 2)

    def __init__(self, gene_list):
        self.gene_list = [closest(gene_list[0], self.x_set), closest(gene_list[1], self.y_set)]

    def __str__(self):
        return str(self.gene_list)


def create_random():
    return Individual([random.choice(Individual.x_set), random.choice(Individual.y_set)])


if __name__ == '__main__':

    random.seed(3)

    ind1 = create_random()
    ind2 = create_random()
    print(f'Individual 1: {ind1}')
    print(f'Individual 2: {ind2}')

    c1_genes, c2_genes = crossover_blend(ind1.gene_list, ind2.gene_list, 0.2)
    child1, child2 = Individual(c1_genes), Individual(c2_genes)
    print(f'Child 1: {child1}')
    print(f'Child 1: {child2}')

    mut1 = Individual(mutation_random_deviation(child1.gene_list, 0, 2, .5))
    mut2 = Individual(mutation_random_deviation(child2.gene_list, 0, 2, .5))
    print(f'Mutant 1: {mut1}')
    print(f'Mutant 2: {mut2}')
