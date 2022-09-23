import pandas as pd

def get_neutral(home_team, away_team):
    """this function returns if the game is neutral

    Arguments:
        home_team {str} -- home team
        away_team {str} -- away team

    Returns:
        bool -- Yes or No the game is neutral
    """
    if home_team=="Qatar":
        return False
    elif away_team=="Qatar":
        return False
    else:
        return True

fr = pd.read_csv('../data/fifa_ranking.csv', sep=',', decimal='.')

def get_confederation(team):
    """the confederation of the team

    Arguments:
        team {str} -- The team

    Returns:
        str -- Confederation of the team
    """
    conf = fr.loc[fr.countr_full==team, 'confederation'].unique()[0]
    return conf