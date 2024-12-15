# v0.py
* `get_player_data(name : str)` will return a string. This needs to be loaded to JSON to be parsed
    * Keys will then be filters, teams, categories, and glossary. We care mostly about categories, as this contains the statistics
    * Categories will return a list of dictionary values. Can ensure keys match with lambda function on first key equality combined with a map func and all func
    * Categories differ based on statistic description, which is in top level "name" key


sample game id: 401437933, Arizona @ Atlanta (ATL_ID : 1, ARI_ID : 22)
sampel player id: 


# reqESPN.get_game_summary(game_id)
* keys:
    * boxscore
        * teams : list of 2 team objects, keys below
            * team, statistics, displayOrder, homeAway
            * JSON stubs (3-6 kv pairs)
        * players : list of 2 team objects
            * team, statistics, displayOrder, homeAway
            * statistics obj keys:
                * name : name of statistical category
                * keys : name of each statistical index
                * text : <Team Name> <Statistic Name>
                * labels : keys, but abbreviated
                * athletes : statiscial earners, another object
                    * athlete : dict_keys(['id', 'uid', 'guid', 'firstName', 'lastName', 'displayName', 'links', 'jersey'])
                    * stats : list<num> containing statistical values
            * larger JSON results, all players on a team logging statistics

    * gameInfo
        * venue, attendance, officials

    * drives
        * previous, current (if game is live)
            *  list of drives, homogenous keys
            * keys: ['id', 'description', 'team', 'start', 'end', 'timeElapsed', 'yards', 'isScore', 'offensivePlays', 'result', 'shortDisplayResult', 'displayResult', 'plays']
    
    * odds
        * empty if game is previous
        * live?

    * scoringPlays
        * list of scoring plays, homogenous keys
        * 'id', 'type', 'text', 'awayScore', 'homeScore', 'period', 'clock', 'team', 'scoringType'

    * standings
        * fullLinkView, groups
            * fullLinkView is for browser
            * groups is a list [Team 1 Division, Team 2 Division]
                * sample in "standings_groups.json"