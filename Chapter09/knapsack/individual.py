import random
from itertools import compress


class Item:

    def __init__(self, name, weight, price) -> None:
        self.name = name
        self.weight = weight
        self.price = price


class Individual:
    counter = 0

    @classmethod
    def set_items(cls, items):
        cls.items = items

    @classmethod
    def set_max_weight(cls, max_weight):
        cls.max_weight = max_weight

    @classmethod
    def create_random(cls):
        return Individual([random.choice([0, 1]) for _ in range(len(cls.items))])

    def __init__(self, gene_list) -> None:
        self.gene_list = gene_list
        self.fitness = self.fitness_function()
        self.__class__.counter += 1

    def total_price(self):
        return sum([i.price for i in list(compress(self.__class__.items, self.gene_list))])

    def total_weight(self):
        return sum([i.weight for i in list(compress(self.__class__.items, self.gene_list))])

    def fitness_function(self):
        if self.total_weight() > self.__class__.max_weight:
            return 0
        else:
            return self.total_price()

    def __str__(self):
        return f'gene: {self.gene_list}, price: {self.total_price()}, weight: {self.total_weight()}'

    def plot_info(self):
        print(f'Included: {[i.name for i in list(compress(self.__class__.items, self.gene_list))]}')
        print(f'Fitness: {self.fitness}')
        print(f'Price: {self.total_price()}')
        print(f'Weight: {self.total_weight()}')


if __name__ == '__main__':

    random.seed(13)

    items = [
        Item('laptop', 3, 300),
        Item('book', 2, 15),
        Item('radio', 1, 30),
        Item('tv', 6, 230),
        Item('potato', 5, 7),
        Item('brick', 3, 1),
        Item('bottle', 1, 2),
        Item('camera', 0.5, 280),
        Item('smartphone', 0.1, 500),
        Item('picture', 1, 170),
        Item('flower', 2, 5),
        Item('chair', 3, 4),
        Item('watch', 0.05, 500),
        Item('boots', 1.5, 30),
        Item('radiator', 5, 25),
        Item('tablet', 0.5, 450),
        Item('printer', 4.5, 170)
    ]

    Individual.set_items(items)
    Individual.set_max_weight(10)

    ind = Individual.create_random()

    ind.plot_info()
