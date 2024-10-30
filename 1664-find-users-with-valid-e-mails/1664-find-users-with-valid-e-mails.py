import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[A-Za-z][A-Za-z0-9\._-]*@leetcode\.com$'
    output = users[users['mail'].str.contains(pattern)]

    return output
        