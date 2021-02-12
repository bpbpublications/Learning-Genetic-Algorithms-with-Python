import random
from ch10.tsp.route import distance, get_us_capitals, plot_route


class Individual:
    count = 0
    points = []

    def __init__(self, gene_list) -> None:
        self.gene_list = gene_list
        self.fitness = self.fitness_function()
        self.__class__.count += 1

    def fitness_function(self):
        return -distance(self.points, self.gene_list)


def generate_random(points_num):
    route = list(range(points_num))
    random.shuffle(route)
    return Individual(route)


if __name__ == '__main__':
    random.seed(1)
    points = get_us_capitals()
    Individual.points = points
    ind = generate_random(len(points))
    plot_route(points, ind.gene_list)
