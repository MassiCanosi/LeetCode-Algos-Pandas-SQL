import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df_adj = pd.merge(customers,orders,how='left', left_on='id', right_on='customerId')
    df_final = pd.DataFrame(df_adj[df_adj['customerId'].isna()].iloc[:,1])
    otp = df_final.rename(columns={'name': 'Customers'})
    return otp