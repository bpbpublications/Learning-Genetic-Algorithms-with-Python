import random


class EnumeratedIndividual:
    x_set = ['A', 'B', 'C', 'D']

    def __init__(self, gene_list):
        self.gene_list = gene_list

    def __str__(self):
        return str(self.gene_list)


def create_random():
    return EnumeratedIndividual([random.choice(EnumeratedIndividual.x_set)])


def crossover(p1, p2):
    return EnumeratedIndividual([p2[0]]), EnumeratedIndividual([p1[0]])


def mutation(ind):
    return EnumeratedIndividual([random.choice(EnumeratedIndividual.x_set)])
