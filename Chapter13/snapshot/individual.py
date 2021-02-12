import json
import random


class Individual:

    def __init__(self, gene_list) -> None:
        self.gene_list = gene_list


def dump_population(population, path):
    ind_genes = [ind.gene_list for ind in population]
    with open(path, 'w') as f:
        json.dump(ind_genes, f)


def restore_population(path):
    population = []
    with open(path) as json_file:
        ind_genes = json.load(json_file)
        for gene_list in ind_genes:
            population.append(Individual(gene_list))
    return population


if __name__ == '__main__':

    population = [Individual([random.randint(0, 100)]) for _ in range(100)]
    path = '/tmp/population_genes.json'
    dump_population(population, path)
    restored_population = restore_population(path)
