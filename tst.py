import v0

bal = v0.team_pipeline("BAL")

def bld_df(st):
    import pandas as pd
    import pdb; pdb.set_trace()
    df = pd.DataFrame()
    for a, s in st['athleteStats'].items():
        df = pd.concat([df, pd.DataFrame([a] + s).T])
    return df

bld_df(bal[0]['Baltimore Passing'])