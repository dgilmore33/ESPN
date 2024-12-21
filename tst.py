import v0

bal = v0.team_pipeline("BAL")

def bld_df_from_player_stats(st):
    import pandas as pd
    # import pdb; pdb.set_trace()
    df = pd.DataFrame()
    for a, s in st['athleteStats'].items():
        df = pd.concat([df, pd.DataFrame([a] + s).T])
    df.rename(columns=dict(zip(df.columns, ['playerName'] + st['keys'])), inplace=True)
    return df

df = bld_df_from_player_stats(bal[0]['Baltimore Passing'])