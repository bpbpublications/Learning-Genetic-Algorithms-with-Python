class Individual:
    cache = {}
    cache_hit = 0
    counter = 0

    @classmethod
    def set_fitness_function(cls, fun):
        cls.fitness_function = fun

    def __init__(self, gene_list) -> None:
        coarsed_gene_list = [round(g) for g in gene_list]
        self.gene_list = coarsed_gene_list
        gene_hash = ','.join([str(g) for g in coarsed_gene_list])
        cache = self.__class__.cache
        if gene_hash not in cache.keys():
            cache[gene_hash] =\
                self.__class__.fitness_function(coarsed_gene_list)
        else:
            self.__class__.cache_hit += 1

        self.fitness = cache[gene_hash]
        self.__class__.counter += 1
