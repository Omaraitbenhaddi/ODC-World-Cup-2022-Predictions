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

fr = pd.read_csv('./data1/fifa_ranking.csv', sep=',', decimal='.')
fr['year'] = fr.apply(lambda x: x.rank_date[:4], axis=1)
fr['month'] = fr.apply(lambda x: x.rank_date[5:7], axis=1)
d_rank = fr.query('year=="2022" and month=="08"')
d_points = fr.query('year=="2022" and month=="08"')[['rank', 'country_full', 'total_points']]

#--------------------------------------------------------------------------------------------


def get_confederation(team):
    """the confederation of the team

    Arguments:
        team {str} -- The team

    Returns:
        str -- Confederation of the team
    """
    conf = fr.loc[fr.country_full==team, 'confederation'].unique()[0]
    return conf



#-------------------------------------------------------------------------------------------



def get_tier(team):
    """_ the tier of the team

    Args:
        team (str): the team

    Returns:
        str: tier of the team
    """
    r = fr.loc[(fr.country_full==team) & (fr.year=="2022") & (fr.month=="08"), 'rank'].iloc[0]
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
    home_points = fr.loc[(fr.country_full==home_team) & (fr.year=="2022") & (fr.month=="08"), 'total_points'].iloc[0]
    away_points = fr.loc[(fr.country_full==away_team) & (fr.year=="2022") & (fr.month=="08"), 'total_points'].iloc[0]
    
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


def get_match(home_team, away_team, predictors, xcols):
    #home_team
    #away_team

    neutral = get_neutral(home_team, away_team)
    confederation = get_confederation(home_team)
    confederation__away = get_confederation(away_team)
    home_tier = get_tier(home_team)
    away_tier = get_tier(away_team)
    marginal_effect_ = marginal_effect(home_team, away_team)
    effect_tier_ = effect_tier(home_team, away_team)
    match_importance=1


    match = [home_team, away_team, neutral, confederation, confederation__away, home_tier, away_tier, marginal_effect_, effect_tier_,match_importance]

    d_match = pd.DataFrame([match], columns=predictors)

    x_match = pd.get_dummies(d_match)

    for col in xcols:
        if col not in x_match:
            x_match[col] = 0

    return x_match[xcols]



def get_match_proba(home_team,away_team,model,predictors,xcols):
    pred={
        'draw':None,
        home_team:None,
        away_team:None
    }
    pred1=model.predict_proba(get_match(home_team,away_team,predictors,xcols))
    pred2=model.predict_proba(get_match(away_team,home_team,predictors,xcols))
    pred['draw']=(pred1[0][0]+pred2[0][0])/2
    pred[home_team]=(pred1[0][2]+pred2[0][1])/2
    pred[away_team]=(pred1[0][1]+pred2[0][2])/2
    return pred
    
def get_winner(home_team,away_team,model,predictors,xcols):
    dict=get_match_proba(home_team,away_team,model,predictors,xcols)
    print(dict)
    max_prob=0
    for key,value in zip(dict.keys(),dict.values()):
        if(value>max_prob):
            win=key
            max_prob=value
    return win

