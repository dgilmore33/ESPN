import reqESPN
import pandas as pd
from pprint import pprint

plyr_kys = pd.read_csv('/Users/danielgilmore/Scripts/ESPN/player_id .csv')

lookup = lambda id : reqESPN.getStats_frID(id)

"""
    returns a json with keys
        'filters', 'teams', 'categories', 'glossary'

"""

def get_player_data(name):
    return lookup(plyr_kys[plyr_kys['Name'] == name].values[0][0])

def parse_player_cats(json):
    cats = json['categories']

    zipStats = lambda statlst, lbl : { k : v for k, v in zip(lbl, statlst)} 

    statPack = { x['name'] : zipStats(x['totals'], x['labels']) for x in cats }