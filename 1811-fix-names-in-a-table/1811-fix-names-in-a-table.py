import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].apply(lambda x: str(x[0].upper()) + str(x[1:].lower()))
    return users.sort_values(by='user_id')