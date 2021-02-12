import random

from ch10.football_manager.football import get_players, team_price, team_skill, position_violations


class Individual:
    team_size = 23

    @classmethod
    def set_fitness_function(cls, fun):
        cls.fitness_function = fun

    def __init__(self, gene_list) -> None:
        self.gene_list = gene_list
        self.fitness = self.__class__.fitness_function(self.get_team())

    def get_team(self):
        return self.gene_list[:self.__class__.team_size]


def generate_random(base_size):
    players_idx = list(range(base_size))
    random.shuffle(players_idx)
    return Individual(players_idx)


if __name__ == '__main__':

    player_base_df = get_players()


    def fitness_function(team):
        global player_base_df
        min_positions = {'G': 2, 'D': 5, 'M': 5, 'F': 4}
        max_positions = {'G': 3, 'D': 7, 'M': 7, 'F': 5}
        skills = team_skill(player_base_df, team)
        if not position_violations(player_base_df, team, min_positions, max_positions):
            return skills * 0.5
        if team_price(player_base_df, team) > 500_000_000:
            return 0
        return skills


    Individual.set_fitness_function(fitness_function)
    ind = generate_random(len(player_base_df))

    print(ind.fitness)
