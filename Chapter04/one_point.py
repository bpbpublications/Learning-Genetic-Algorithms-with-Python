import copy
import random


def crossover_one_point(p1, p2):
    point = random.randint(1, len(p1) - 1)
    c1, c2 = copy.deepcopy(p1), copy.deepcopy(p2)
    c1[point:], c2[point:] = p2[point:], p1[point:]
    return [c1, c2]


random.seed(2)

p1 = [random.randint(0, 9) for _ in range(5)]
p2 = [random.randint(0, 9) for _ in range(5)]

offspring = crossover_one_point(p1, p2)

print(f'Parent 1: {p1}')
print(f'Parent 2: {p2}')
print(f'Child 1: {offspring[0]}')
print(f'Child 2: {offspring[1]}')
