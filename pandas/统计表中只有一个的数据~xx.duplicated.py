import pandas as pd


def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    # df = employee[(employee['primary_flag'] == 'Y') | ~(employee['employee_id'].duplicated(keep=False))].drop(columns='primary_flag')
    df = employee[(employee['primary_flag'] == 'Y') | ~(employee['employee_id'].duplicated(keep=False))][['employee_id', 'department_id']]
    return df


data = [['1', '1', 'N'], ['2', '1', 'Y'], ['2', '2', 'N'], ['3', '3', 'N'], ['4', '2', 'N'], ['4', '3', 'Y'], ['4', '4', 'N']]
employee = pd.DataFrame(data, columns=['employee_id', 'department_id', 'primary_flag']).astype({'employee_id':'Int64', 'department_id':'Int64', 'primary_flag':'object'})

print(find_primary_department(employee))
