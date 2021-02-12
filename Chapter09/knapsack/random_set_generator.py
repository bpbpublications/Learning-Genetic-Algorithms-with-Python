import random
import matplotlib.pyplot as plt

from ch9.knapsack.individual import Item


def random_set_generator(min_price, max_price, min_weight, max_weight, total_number):
    l = []
    for i in range(total_number):
        l.append(Item(f'Item#{i}', random.uniform(min_weight, max_weight), random.uniform(min_price, max_price)))
    return l


if __name__ == '__main__':
    random.seed(15)
    items = random_set_generator(1, 100, 0.1, 7, 200)
    plt.scatter([i.weight for i in items], [i.price for i in items])
    plt.xlabel('weight')
    plt.ylabel('price')
    plt.show()
