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


#--------------------------------------------------------------------------------------------


def get_confederation(team):
    """the confederation of the team

    Arguments:
        team {str} -- The team

    Returns:
        str -- Confederation of the team
    """
    conf = fr.loc[fr.countr_full==team, 'confederation'].unique()[0]
    return conf



#-------------------------------------------------------------------------------------------



def get_tier(team):
    """_ the tier of the team

    Args:
        team (str): the team

    Returns:
        str: tier of the team
    """
    r = d_rank.loc[d_rank.country_full==team, 'rank'].iloc[0]
    if r <= 8:
        return 'diamond'
    elif r <= 16:
        return 'gold'
    elif r <= 32:
        return 'silver'
    else:
        return 'bronze'
    
    
    
#--------------------------------------------------------------------------------------------


def marginal_effect(home_team, away_team):
    """_ marginal effect

    Args:
        home_team (str): home team
        away_team (str): away team
    Returns:
        float: marginal effect 
    """
    home_points = d_points.loc[d_points.country_full==home_team, 'total_points'].iloc[0]
    away_points = d_points.loc[d_points.country_full==away_team, 'total_points'].iloc[0]
    
    return (home_points - away_points) / away_points


#--------------------------------------------------------------------------------------------

