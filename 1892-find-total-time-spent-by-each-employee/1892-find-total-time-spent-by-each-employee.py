import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employee_adj = employees.rename(columns={'event_day': 'day'})

    employee_adj['total_time'] = employee_adj['out_time'] - employee_adj['in_time']

    output = employee_adj.pivot_table(index=['day', 'emp_id'], values='total_time', aggfunc='sum').reset_index()

    return output