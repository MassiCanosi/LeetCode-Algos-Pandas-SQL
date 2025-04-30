import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity_adj = activity[['player_id', 'event_date']].drop_duplicates()
    output = activity_adj.groupby(by='player_id').min().reset_index().rename(columns={'event_date': 'first_login'})

    return pd.DataFrame(output)
    