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
    r = fr.d_rank.loc[fr.d_rank.country_full==team, 'rank'].iloc[0]
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
    home_points = fr.d_points.loc[fr.d_points.country_full==home_team, 'total_points'].iloc[0]
    away_points = fr.d_points.loc[fr.d_points.country_full==away_team, 'total_points'].iloc[0]
    
    return (home_points - away_points) / away_points


#--------------------------------------------------------------------------------------------



def effect_tier(home_team, away_team):
    
    """based on marginal_effect we classify teams _very__high, high, medium, low_

        Arguments:
            home_team {str} -- The home team
            away_team {str} -- The away team

        Returns:
            str -- effect tier "low" or "medium" or "high" or "very high"
        """

    marginal_eff = marginal_effect(home_team, away_team)

    if marginal_eff < -0.37:
        return 'low'
    elif marginal_eff >=-0.37 and marginal_eff < -0.20:
        return 'medium'
    elif marginal_eff >=-0.20 and marginal_eff < -0.25:
        return 'high'
    else:
        return 'very_high'


