import v0
import parseESPN
import reqESPN

# lj = v0.get_player_data("Lamar Jackson")
# lj_stats = parseESPN.parse_stats_from_player(lj)


from datetime import date, datetime

today = date.today()

import json

team_sched_js = json.loads(reqESPN.get_tmSched(1))

d8s = [x for x in team_sched_js['events'] if datetime.strptime(x['date'], "%Y-%m-%dT%H:%MZ") < 
                                                datetime.strptime(str(today), "%Y-%m-%d")]

# str = reqESPN.get_gm_summary(401437933)

