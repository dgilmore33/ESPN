import reqESPN
import pandas as pd
from pprint import pprint
import parseESPN

plyr_kys = pd.read_csv('/Users/danielgilmore/Scripts/ESPN/player_id .csv')

team_kys = pd.read_csv('team_id.csv')

lookup_player = lambda id : reqESPN.getStats_frID(id)
lookup_team_id = lambda abbreviation: team_kys[team_kys['TEAM ABBREVIATION'] == abbreviation]\
                                              .TEAMID.values[0]

"""
    returns a json with keys
        'filters', 'teams', 'categories', 'glossary'

"""

def get_player_data(name):
    return lookup_player(plyr_kys[plyr_kys['Name'] == name].values[0][0])




# Bad Function

# def parse_player_cats(json):
#     cats = json['categories']

#     zipStats = lambda statlst, lbl : { k : v for k, v in zip(lbl, statlst)} 

#     statPack = { x['name'] : zipStats(x['totals'], x['labels']) for x in cats }

#     return statPack

def prev_sched(sched):
    from datetime import date, datetime

    today = date.today()

    import json

    team_sched_js = json.loads(sched)

    d8s = [x for x in team_sched_js['events'] if datetime.strptime(x['date'], "%Y-%m-%dT%H:%MZ") < 
                                                    datetime.strptime(str(today), "%Y-%m-%d")]

    return d8s

def team_pipeline(abbreviation:str):
    
    tm_id = lookup_team_id(abbreviation=abbreviation)

    sched = reqESPN.get_tmSched(tm_id)

    ps = prev_sched(sched)

    ids = [x['id'] for x in ps]

    gms = [reqESPN.get_gm_summary(id) for id in ids]

    plyr_box_scores = [parseESPN.summary_to_player(gm) for gm in gms]

    return plyr_box_scores
    # return(ps)

def bld_df_from_player_stats(st):
    df = pd.DataFrame()
    for a, s in st['athleteStats'].items():
        df = pd.concat([df, pd.DataFrame([a] + s).T])
    return df
