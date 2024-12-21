import requests
import json
from pprint import pprint


# region ESPN API references
"""  Github References :  """
""" https://gist.github.com/nntrn/ee26cb2a0716de0947a0a4e9a157bc1c """
"""    * https://github.com/pick-em/data-extract/wiki/ESPN-APIs """
"""    * https://github.com/ianpherbert/ESPN-API-Documentation/blob/master/endpoints.txt#L77 """
# endregion

base = "http://site.api.espn.com/apis/site/v2/sports/football/nfl"


def simple_request(url:str):
    get = requests.get(url)

    if get.status_code != 200:
        raise Warning("Not `OK 200` response")

    return get.text

# region METHODS that QUERY on ID 
def getEv_frID(id):
    return simple_request(f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/{id}")
   

# TODO :: getOdds_frID function that queries http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/401547654/competitions/401547654/odds
def getOdds_frID(id):
    return simple_request(f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/{id}/competitions/{id}/odds")

def getOdds_frID(id):
    return simple_request(f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/{id}/competitions/{id}/odds")

""" 
    Return player API Endpoint
 """
def getPlyr_frID(id):
    return simple_request(f"https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/{id}")

""" 
    Return player stats API Endpoint

    @param id : player id
 """
def getStats_frID(id):
    return simple_request(f"https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/{id}/stats")

""" 
    Return team stat API Endpoint

    @param year : year of season
    @param id : team id
 """
def getStat_frTm(year, id):
    return simple_request(f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{year}/teams/{id}")


def get_tmSched(id):
    return simple_request(f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/{id}/schedule")

def get_pbp(id):
    return simple_request(f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/{id}/competitions/{id}/plays?limit=300")

def get_plyr_szn(year:int, id:str):
    return simple_request(f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{year}/athletes/{id}/eventlog")

def get_plyr_game(player_id, game_id, team_id):
    return simple_request(f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/{game_id}/competitions/{game_id}/competitors/{team_id}/roster/{player_id}/statistics/0?lang=en&region=us")

def get_gm_summary(game_id):
    return simple_request(f"http://site.web.api.espn.com/apis/site/v2/sports/football/nfl/summary?event={game_id}")

# endregion

# region METHODS that QUERY on OTHER

def getWk_frSnType(year):
    return simple_request(f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{year}/types/1/weeks")

def getEv_frWk(year, wk):
    return simple_request(f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{year}/types/2/weeks/{wk}/events")

# endregion
