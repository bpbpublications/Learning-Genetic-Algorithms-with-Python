import copy
import random


def crossover_blend(p1, p2, alpha):
    c1 = copy.deepcopy(p1)
    c2 = copy.deepcopy(p2)

    for i in range(len(p1)):
        l = min(c1[i], c2[i]) - alpha * abs(c2[i] - c1[i])
        u = max(c1[i], c2[i]) + alpha * abs(c2[i] - c1[i])
        c1[i] = round(l + random.random() * (u - l), 2)
        c2[i] = round(l + random.random() * (u - l), 2)

    return [c1, c2]


random.seed(3)

p1 = [round(random.uniform(0, 10), 2) for _ in range(6)]
p2 = [round(random.uniform(0, 10), 2) for _ in range(6)]

offspring = crossover_blend(p1, p2, 0.5)

print(f'Parent 1: {p1}')
print(f'Parent 2: {p2}')
print(f'Child 1: {offspring[0]}')
print(f'Child 2: {offspring[1]}')
