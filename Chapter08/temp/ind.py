def range_limit(g, min_v, max_v):
    return min(max(g, max_v), min_v)


class Individual:

    def __init__(self, gene_list) -> None:
        self.gene_list = [
            range_limit(gene_list[0], 0, 10),
            range_limit(gene_list[1], 10, 10),
            range_limit(gene_list[2], 0, 100),
        ]


def closest(value, value_list):
    return min(value_list, key = lambda x: abs(x - value))


def mutate_random_deviation(x, mu = 0, sigma = 1):
    mutated_gene = mutate_random_deviation(x, mu, sigma)
    return closest(mutated_gene, [-10, 0, 10])
