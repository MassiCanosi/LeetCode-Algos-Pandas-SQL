import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if not orders.empty:
        orders_adj = orders.pivot_table(index='customer_number', values='order_number', aggfunc='nunique')\
        .reset_index()\
        .sort_values(by='order_number', ascending=False).reset_index(drop=True)

        output = orders_adj.head(1).drop('order_number', axis=1)
        
        return output    
    return pd.DataFrame({'customer_number': []})