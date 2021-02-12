import random

def selection_tournament(individuals, group_size = 2):
    selected = []
    for _ in range(len(individuals)):
        candidates = [random.choice(individuals) for _ in range(group_size)]
        selected.append(max(candidates, key = lambda ind: ind.fitness))
    return selected

