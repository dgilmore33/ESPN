import requests
import json
from pprint import pprint


# ESPN API
"""  Github References :  """
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




