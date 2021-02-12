import copy
import random


def crossover_uniform(p1, p2, prop):
    c1 = copy.deepcopy(p1)
    c2 = copy.deepcopy(p2)

    for i in range(len(p1)):
        if random.random() < prop:
            c1[i], c2[i] = p2[i], p1[i]

    return [c1, c2]


random.seed(3)

p1 = [random.randint(0, 9) for _ in range(6)]
p2 = [random.randint(10, 19) for _ in range(6)]

offspring = crossover_uniform(p1, p2, 0.5)

print(f'Parent 1: {p1}')
print(f'Parent 2: {p2}')
print(f'Child 1: {offspring[0]}')
print(f'Child 2: {offspring[1]}')
