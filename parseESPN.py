import json


"""
Description: 
Given a string representing the json return from an ESPN API call, 
parse statistics for a player into a digestible format

Input: 
* player_resp : str

Output:
player_stats : 
(dict)
{ (str) category name : (dict) 
    { (str) stat name : 
        (dict) 
        { 
          (str) year played : 
          (num) statistic 
        }
    } 
}
"""
def parse_stats_from_player(player_resp : str):
    js = json.loads(player_resp)

    cats = js['categories']

    one_key = cats[0].keys()
    
    if not all(map(lambda x: x.keys() == one_key,
                    cats)):
        Warning(cats)
        Exception("Non-homogenous Key error!")
    
    d = {}

    for cat in cats:
        
        # import pdb; pdb.set_trace()
        ld = {}
        for season in cat['statistics']:
            ld[season['season']['displayName']] = season['stats']

        d[cat['displayName']] = (cat['displayNames'], ld)

    return d

"""
based off the below url
http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/401671789/competitions/401671789/competitors/33/roster/3916387/statistics/0?lang=en&region=us
schema:
base / events / {event_id} / competitions / {event_id} / competitors / {team_id} / roster / {player_id}
     /statistics/0?lang=en&region=us
"""
# def parse_plyr_event():

def summary_parse(summ : str):
    js = json.loads(summ)

    return js

def parse_gm_box_player(js):
    if type(js) == str:
        js = json.loads(js)
    
    # TODO:: remove hotfix with more streamlined soln
    js = js['boxscore']['players']
    
    cats = ['passing', 
            'rushing', 
            'receiving', 
            'fumbles', 
            'defensive', 
            'interceptions', 
            'kickReturns', 
            'puntReturns', 
            'kicking', 
            'punting']
    
    d1 = {}
    for tm in js:
        for i, cat in enumerate(cats):
            # import pdb; pdb.set_trace()
            try:
                curr = tm['statistics'][i]

            except KeyError as e:
                print(tm.keys())
                print(e)
                print(cat)
                continue
            text : str = curr['text'] # <Team Name> <Statistical Category>

            keys = curr['keys']

            d2 = {}
        
            for a in curr['athletes']:
                d2[a['athlete']['displayName']] = a['stats']

            d1[text] = { "keys":keys, "athleteStats":d2 }
        
    return d1

def summary_to_player(summ):
    # import pdb; pdb.set_trace()

    sp = summary_parse(
            summ=summ
        )

    return parse_gm_box_player(
        sp
    )

def parse_gm_box_team(js):
    if type(js) == str:
        js = json.loads(js)
    gm = {}
    for ob in js:
        js_tm = ob['team']

        tmStats = {x['name']:x['displayValue'] for x in js_tm['statistics']}
        gm[js_tm['displayName']] = tmStats

    return gm