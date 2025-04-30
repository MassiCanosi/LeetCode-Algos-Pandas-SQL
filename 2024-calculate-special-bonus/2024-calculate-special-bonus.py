import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame):
    full_bonus = employees[employees['employee_id'].apply(lambda x: x %2 != 0) & employees['name'].apply(lambda x: str(x)[0] != 'M')].iloc[:,0].tolist()

    employees['bonus'] = 0

    for i,row in employees.iterrows():
        if row['employee_id'] in full_bonus:
            employees.at[i, 'bonus'] = row['salary']

    cols = ['employee_id', 'bonus']

    return pd.DataFrame(employees[cols].sort_values(by='employee_id'))


