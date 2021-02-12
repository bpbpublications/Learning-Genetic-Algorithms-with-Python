import random

from ch10.football_manager.football import (
    get_players, team_skill, team_price, position_violations, team_print,
    team_age,
)
from ch10.football_manager.individual import Individual, generate_random
from ch10.football_manager.toolbox import (
    selection_rank_with_elite,
    crossover_operation,
    mutation_operation,
    stats,
    plot_stats,
    mutation_fitness_driven_shift,
    crossover_fitness_driven_order,
)


def crossover(parent1, parent2):
    return crossover_fitness_driven_order(parent1, parent2)


def mutate(ind):
    return mutation_fitness_driven_shift(ind)


def select(population):
    return selection_rank_with_elite(population, elite_size = 2)


player_base_df = get_players()
fitness_cache = {}


def fitness_function(team):
    global player_base_df
    global fitness_cache
    team_str = ','.join([str(i) for i in team])
    if team_str in fitness_cache.keys():
        return fitness_cache[team_str]
    min_positions = {'G': 2, 'D': 5, 'M': 5, 'F': 4}
    max_positions = {'G': 3, 'D': 7, 'M': 9, 'F': 6}
    skills = team_skill(player_base_df, team)
    if team_price(player_base_df, team) > 500_000_000:
        return 0
    age = team_age(player_base_df, team)
    violations = position_violations(player_base_df, team, min_positions, max_positions)
    val = skills * (1 - violations * .1) * (100 - age / 2) / 100
    fitness_cache[team_str] = val
    return val


Individual.team_size = 23
Individual.set_fitness_function(fitness_function)

random.seed(3)

POPULATION_SIZE = 400
CROSSOVER_PROBABILITY = .3
MUTATION_PROBABILITY = .8
MAX_GENERATIONS = 400

first_population = [generate_random(len(player_base_df)) for _ in range(POPULATION_SIZE)]
best_ind = random.choice(first_population)
fit_avg = []
fit_best = []
generation_num = 0
population = first_population.copy()
generation_number = 0

while generation_num < MAX_GENERATIONS:
    generation_num += 1
    offspring = selection_rank_with_elite(population, elite_size = 2)
    crossed_offspring = crossover_operation(offspring, crossover, CROSSOVER_PROBABILITY)
    mutated_offspring = mutation_operation(crossed_offspring, mutate, MUTATION_PROBABILITY)
    population = mutated_offspring.copy()
    best_ind, fit_avg, fit_best = stats(population, best_ind, fit_avg, fit_best)
    print(
        f'Generation {generation_num}. '
        f'Avg fit: {round(fit_avg[-1], 2)}. '
        f'Best fit: {round(best_ind.fitness,2)}. '
        f'Skills: {team_skill(player_base_df, best_ind.get_team())} '
        f'Price: {team_price(player_base_df, best_ind.get_team())} '
        f'Age: {team_age(player_base_df, best_ind.get_team())}')

    if generation_num % 25 == 0:
        team_print(player_base_df, best_ind.get_team())

plot_stats(fit_avg, fit_best, "Football Manager Problem")
