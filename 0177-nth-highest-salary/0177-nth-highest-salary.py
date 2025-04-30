import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    
    employee_adj = employee[['salary']].sort_values(by='salary', ascending=False).drop_duplicates().reset_index(drop=True)
    col = f'getNthHighestSalary({N})'
    id_no = len(employee_adj)

    if N <= 0 or N > id_no:
        return pd.DataFrame({col: [None]})

    index = N-1
    value = employee_adj.loc[index, 'salary']

    return pd.DataFrame({col: [value]})