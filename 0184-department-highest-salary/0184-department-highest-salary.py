import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    employee_adj = employee.rename(columns={'name': 'Employee', 'salary': 'Salary'})
    department_adj = department.rename(columns={'id': 'departmentId', 'name': 'Department'})

    merged_df = pd.merge(employee_adj, department_adj, on='departmentId', how='inner')

    df = merged_df[['Department', 'Employee', 'Salary']]
    df['max_salary'] = merged_df.groupby(by='Department')['Salary'].transform('max')

    output = df[df['Salary'] == df['max_salary']].drop('max_salary', axis=1)

    return output
    