import numpy as np


def fitness(x):
    return np.sin(x) - .2 * abs(x)


if __name__ == '__main__':
    from ch2.individual import Individual

    ind = Individual([1], fitness)
    print(f"Individual fitness: {ind.fitness}")
    # prints : 0.6414709848078965
