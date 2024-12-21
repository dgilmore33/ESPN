import reqESPN
from datetime import date, datetime
import json

today = date.today()

"""
team_pipeline_heavy: 
* input
    * id:int, team_id
* output
    * boxscores:list<dict>, results from reqESPN.get_gm_summary for all games to date
"""
def team_pipeline_heavy(id: int):
    team_sched_js = json.loads(reqESPN.get_tmSched(id))

    # get dates that have occurred before today
    d8s = [
            x for x in team_sched_js['events'] if 
                datetime.strptime(x['date'], "%Y-%m-%dT%H:%MZ") < 
                datetime.strptime(str(today), "%Y-%m-%d")
        ]

    # get ids for games that have occurred before today
    ids = [x['id'] for x in d8s]

    # get boxscores for games that have occurred
    boxscores = [json.loads(reqESPN.get_gm_summary(x)) for x in ids]
    
    # region dead code to get text from scoring plays...

    # # get scoring plays for games that have occurred
    # scoringPlays = [x['scoringPlays'] for x in boxscores]

    # # get scoring plays for games that have occurred
    # scoring_texts = [x['text'] for y in scoringPlays for x in y]
    # endregion

    return boxscores

# region more dead code to parse text from scoring plays

# def dump_scoring_texts(scoring_texts):
#     import pickle
#     with open("scoringtexts.pkl", "wb") as f:
#         f.write(pickle.dumps(scoring_texts))

# import re

# run_m = re.compile('(\S*\s\S*) (\d\d?) Yd (\S*(?:[^(]\s\S*)?) (\(.*\))')
# pass_m = re.compile('(\S*\s\S*) (\d\d?) Yd pass from (\S*(?:[^(]\s\S*)?) (\(.*\))')
# kick_m = re.compile('(\S*\s\S*) (\d\d?) Yd Field Goal')

# for txt in scoring_texts:
#     # import pdb; pdb.set_trace()
#     rnm = re.match(run_m, txt)
#     psm = re.match(pass_m, txt)
#     km = re.match(kick_m, txt)
#     for ob in [rnm, psm, km]:
#         if ob is not None:
#             print(ob.groups())
#     if all (map (lambda x: x is None, [rnm, psm, km]) ):
#         print("REGEX ERROR")
#         print(txt)
#     # if rem is None:
#     #     rem = re.match(pass_m, txt)
#     # if rem is None:
#     #     rem = re.match(kick_m, txt)
#     # if rem is None:
#     #     print("REGEX FAIL")
#     #     print(txt)
#     # else:
#     #     groups = rem.groups()
# endregion