import reqESPN
from datetime import date, datetime
import json

today = date.today()

team_sched_js = json.loads(reqESPN.get_tmSched(33))

d8s = [
        x for x in team_sched_js['events'] if 
            datetime.strptime(x['date'], "%Y-%m-%dT%H:%MZ") < 
            datetime.strptime(str(today), "%Y-%m-%d")
      ]

ids = [x['id'] for x in d8s]

boxscores = [json.loads(reqESPN.get_gm_summary(x)) for x in ids]

scoringPlays = [x['scoringPlays'] for x in boxscores]

scoring_texts = [x['text'] for y in scoringPlays for x in y]

def dump_scoring_texts():
    import pickle
    with open("scoringtexts.pkl", "wb") as f:
        f.write(pickle.dumps(scoring_texts))

import re

run_m = re.compile('(\S*\s\S*) (\d\d?) Yd (\S*(?:[^(]\s\S*)?) (\(.*\))')
pass_m = re.compile('(\S*\s\S*) (\d\d?) Yd pass from (\S*(?:[^(]\s\S*)?) (\(.*\))')
kick_m = re.compile('(\S*\s\S*) (\d\d?) Yd Field Goal')

for txt in scoring_texts:
    # import pdb; pdb.set_trace()
    rnm = re.match(run_m, txt)
    psm = re.match(pass_m, txt)
    km = re.match(kick_m, txt)
    for ob in [rnm, psm, km]:
        if ob is not None:
            print(ob.groups())
    if all (map (lambda x: x is None, [rnm, psm, km]) ):
        print("REGEX ERROR")
        print(txt)
    # if rem is None:
    #     rem = re.match(pass_m, txt)
    # if rem is None:
    #     rem = re.match(kick_m, txt)
    # if rem is None:
    #     print("REGEX FAIL")
    #     print(txt)
    # else:
    #     groups = rem.groups()
