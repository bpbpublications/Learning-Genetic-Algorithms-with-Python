import random

from ch11.graph.graph_utils import adjacent_vertices_same_color_count, get_edges, get_vertices_from_edges, plot_graph


class Individual:
    color_map = {
        0: "red",
        1: "green",
        2: "blue"
    }

    vertex_number = 0
    edges = []

    def __init__(self, gene_list) -> None:
        self.gene_list = gene_list
        self.fitness = - adjacent_vertices_same_color_count(self.__class__.edges, self.vertex_colors())

    def vertex_colors(self):
        vertex_colors = {}
        for i in range(len(self.gene_list)):
            vertex_colors[i] = self.__class__.color_map[self.gene_list[i]]
        return vertex_colors

    @classmethod
    def generate_random(cls):
        gene_list = random.choices(list(cls.color_map.keys()), k = cls.vertex_number)
        return Individual(gene_list)


if __name__ == '__main__':

    random.seed(1)

    edges = get_edges()
    Individual.vertex_number = len(get_vertices_from_edges(edges))
    Individual.edges = edges

    ind = Individual.generate_random()
    print(f'Fitness: {ind.fitness}')
    plot_graph(Individual.edges, ind.vertex_colors())
