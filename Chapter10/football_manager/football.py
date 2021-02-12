import random

import pandas as pd


# https://www.kaggle.com/stefanoleone992/fifa-20-complete-player-dataset
def get_players():
    df = pd.read_csv('players_20.csv')
    df.drop(df.columns.difference(
        ['short_name', 'value_eur', 'team_position', 'overall', 'club', 'age']), 1, inplace = True)
    df.rename(columns = {'short_name': 'name', 'value_eur': 'price', 'team_position': 'position', 'overall': 'skills'},
              inplace = True)
    position_map = {
        "RW":  "M", "LW": "M", "CAM": "F", "GK": "G", 'RCM': 'M', 'LCB': 'D', 'ST': 'F', 'CDM': 'M', 'LDM': 'M',
        'RM':  'M', 'RCB': 'D', 'LCM': 'M', 'LM': 'M', 'CF': 'F', 'LB': 'D', 'LS': 'D', 'RB': 'D', 'RDM': 'M',
        'RAM': 'M', 'RS': 'D', 'RF': 'F', 'CM': 'M', 'CB': 'D', 'LF': 'F', 'LAM': 'M', 'RWB': 'D', 'LWB': 'D'
    }
    df.replace({"position": position_map}, inplace = True)
    df = df[(df['skills'] > 75) & (df['position'].isin(position_map.values()))]
    return df


def position_violations(players_df, team, min_positions, max_positions):
    team_df = players_df[players_df.index.isin(team)]
    team_positions = {}
    for _, row in team_df.iterrows():
        pos = row['position']
        if pos in team_positions.keys():
            team_positions[pos] += 1
        else:
            team_positions[pos] = 1

    violations = 0

    for k in list(min_positions.keys()):
        if k not in team_positions.keys() or min_positions[k] > team_positions[k]:
            violations += 1

    for k in list(max_positions.keys()):
        if k not in team_positions.keys() or max_positions[k] < team_positions[k]:
            violations += 1

    return violations


def team_price(players_df, team):
    team_df = players_df[players_df.index.isin(team)]
    return team_df['price'].sum()


def team_skill(players_df, team):
    team_df = players_df[players_df.index.isin(team)]
    return round(team_df['skills'].sum() / len(team), 2)


def team_age(players_df, team):
    team_df = players_df[players_df.index.isin(team)]
    return round(team_df['age'].sum() / len(team), 2)


def team_print(players_df, team):
    position_map = {
        'G': 'Goalkeepers',
        'D': 'Defenders',
        'M': 'Midfielders',
        'F': 'Forwards'
    }

    for k, v in position_map.items():
        print(f'\n{v}:')
        team_df = players_df[players_df.index.isin(team)]
        for _, row in team_df[team_df['position'] == k].sort_values(by = 'skills').iterrows():
            print(f"{row['name']} ({row['club']}). "
                  f"Skill: {row['skills']}. Price: {'{:,}'.format(row['price'])}. Age: {row['age']}")
