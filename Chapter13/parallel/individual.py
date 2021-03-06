import random


class Individual:
    rows = 0
    cols = 0

    @classmethod
    def set_fitness_function(cls, fun):
        cls.fitness_function = fun

    @classmethod
    def generate_random(cls, radar_prob):
        gene_list = [0] * cls.rows * cls.cols
        for i in range(cls.rows * cls.cols):
            if random.random() < radar_prob:
                gene_list[i] = 1
        return Individual(gene_list)

    def __init__(self, gene_list) -> None:
        self.gene_list = gene_list
        self.fitness = self.__class__.fitness_function(self.get_coordinates())

    def get_coordinates(self):
        r = self.__class__.rows
        c = self.__class__.cols
        matrix = [[None] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                matrix[i][j] = self.gene_list[i * r + j]
        return matrix

    def count_radars(self):
        return sum(self.gene_list)
