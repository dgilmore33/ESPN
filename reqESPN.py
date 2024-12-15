import requests
import json
from pprint import pprint


# ESPN API
"""  Github References :  """
""" https://gist.github.com/nntrn/ee26cb2a0716de0947a0a4e9a157bc1c """
"""    * https://github.com/pick-em/data-extract/wiki/ESPN-APIs """
"""    * https://github.com/ianpherbert/ESPN-API-Documentation/blob/master/endpoints.txt#L77 """

base = "http://site.api.espn.com/apis/site/v2/sports/football/nfl"


################## METHODS that QUERY on ID ##################
def getEv_frID(id):
    get = requests.get("http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/{}"\
                       .format(id))
    
    if get.status_code != 200:
        raise Warning("Not `OK 200` response")
    
    return get.text

# TODO :: getOdds_frID function that queries http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/401547654/competitions/401547654/odds
def getOdds_frID(id):
    get = requests.get(f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/{id}/competitions/{id}/odds")

    if get.status_code != 200:
        raise Warning("Not `OK 200` response")
    
    return get.text

def getOdds_frID(id):
    get = requests.get(f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/{id}/competitions/{id}/odds")

    if get.status_code != 200:
        raise Warning("Not `OK 200` response")
    
    return get.text

""" 
    Return player API Endpoint
 """
def getPlyr_frID(id):
    get = requests.get(f"https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/{id}")

    if get.status_code != 200:
        raise Warning("Not `OK 200` response")
    
    return get.text

""" 
    Return player stats API Endpoint

    @param id : player id
 """
def getStats_frID(id):
    get = requests.get(f"https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/{id}/stats")

    if get.status_code != 200:
        raise Warning("Not `OK 200` response")
    
    return get.text


################## METHODS that QUERY on OTHER ##################

def getWk_frSnType(year):
    get = requests.get(f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{year}/types/1/weeks")

    if get.status_code != 200:
        raise Warning("Not `OK 200` response")
    
    return get.text

def getEv_frWk(year, wk):
    get = requests.get(f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{year}/types/2/weeks/{wk}/events")

    if get.status_code != 200:
        raise Warning("Not `OK 200` response")
    
    return get.text

""" 
    Return team stat API Endpoint

    @param year : year of season
    @param id : team id
 """
def getStat_frTm(year, id):
    get = requests.get(f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{year}/teams/{id}")

    if get.status_code != 200:
        raise Warning("Not `OK 200` response")
    
    return get.text


def get_tmSched(id):
    get = requests.get(f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/{id}/schedule")
    
    if get.status_code != 200:
        raise Warning("Not `OK 200` response")
    
    return get.text

def get_pbp(id):
    get = requests.get(f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/{id}/competitions/{id}/plays?limit=300")

    if get.status_code != 200:
        raise Warning("Not `OK 200` response")
    
    return get.text

def get_plyr_szn(year:int, id:str):
    get = requests.get(f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{year}/athletes/{id}/eventlog")
    
    if get.status_code != 200:
        raise Warning("Not `OK 200` response")
    
    return get.text

def get_plyr_game(player_id, game_id, team_id):
    get = requests.get(f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/{game_id}/competitions/{game_id}/competitors/{team_id}/roster/{player_id}/statistics/0?lang=en&region=us")

    if get.status_code != 200:
        raise Warning("Not `OK 200` response")
    
    return get.text

def get_gm_summary(game_id):
    s = f"http://site.web.api.espn.com/apis/site/v2/sports/football/nfl/summary?event={game_id}"

    get = requests.get(s)

    if get.status_code != 200:
        raise Warning("Not `OK 200` response")
    
    return get.text
