import random

from ch13.caching.individual import Individual
from ch13.caching.schedule_analyzer import shift_deviations, shift_relax
from ch13.caching.toolbox import (
    crossover_n_point, selection_rank_with_elite, mutation_bit_flip, crossover_operation,
    mutation_operation, stats, plot_stats,
)


def crossover(parent1, parent2):
    child1_genes, child2_genes = crossover_n_point(parent1.gene_list, parent2.gene_list, 3)
    return Individual(child1_genes), Individual(child2_genes)


def mutate(ind):
    mutated_gene = mutation_bit_flip(ind.gene_list)
    return Individual(mutated_gene)


def select(population):
    return selection_rank_with_elite(population, elite_size = 2)


if __name__ == '__main__':

    random.seed(3)

    Individual.set_employees(5)
    Individual.set_period(7)


    def fitness_function(df):
        dev = shift_deviations(df,
                               mor_min = 1, mor_max = 4,
                               day_min = 2, day_max = 5,
                               evn_min = 1, evn_max = 2
                               )
        relax = shift_relax(df, 1, 1, 3)
        return -(dev + relax * 5)


    Individual.set_fitness_function(fitness_function)

    POPULATION_SIZE = 30
    CROSSOVER_PROBABILITY = .8
    MUTATION_PROBABILITY = .5
    MAX_GENERATIONS = 200

    first_population = [Individual.generate_random() for _ in range(POPULATION_SIZE)]
    best_ind = random.choice(first_population)
    fit_avg = []
    fit_best = []
    generation_num = 0
    population = first_population.copy()

    while generation_num < MAX_GENERATIONS and best_ind.fitness != 0:
        generation_num += 1
        offspring = select(population)
        crossed_offspring = crossover_operation(offspring, crossover, CROSSOVER_PROBABILITY)
        mutated_offspring = mutation_operation(crossed_offspring, mutate, MUTATION_PROBABILITY)
        population = mutated_offspring.copy()
        best_ind, fit_avg, fit_best = stats(population, best_ind, fit_avg, fit_best)

    plot_stats(fit_avg, fit_best, "Schedule Problem")

    print(f'Total Number of Individuals: {Individual.counter}')
    print(f'Cache Hits: {Individual.cache_hit}')

    best_ind.plot_schedule()
