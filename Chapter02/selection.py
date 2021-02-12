import random

from ch2.individual import create_random_individual


def select_tournament(population, tournament_size):
    new_offspring = []
    for _ in range(len(population)):
        candidates = [random.choice(population) for _ in range(tournament_size)]
        new_offspring.append(max(candidates, key = lambda ind: ind.fitness))
    return new_offspring


if __name__ == '__main__':

    random.seed(29)

    POPULATION_SIZE = 5

    generation_1 = [create_random_individual() for _ in range(POPULATION_SIZE)]
    generation_2 = select_tournament(generation_1, 3)

    print("Generation 1")
    [print(ind) for ind in generation_1]

    print("Generation 2")
    [print(ind) for ind in generation_2]
