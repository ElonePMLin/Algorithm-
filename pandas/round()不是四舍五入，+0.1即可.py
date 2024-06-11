import pandas as pd


def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(employees, left_on='employee_id', right_on='reports_to')
    df = df.groupby(by=['reports_to_y', 'name_x'], as_index=False, dropna=False).agg({
        'name_y': 'size', 'age_y': lambda x: round(x.sum() / x.count() + 0.1)
    }).rename(columns={
        'reports_to_y': 'employee_id', 'name_x': 'name', 'name_y': 'reports_count', 'age_y': 'average_age'
    })
    return df


data = [[9, 'Hercy', None, 43], [6, 'Alice', 9, 41], [4, 'Bob', 9, 36], [2, 'Winston', None, 37]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'reports_to', 'age']).astype({'employee_id':'Int64', 'name':'object', 'reports_to':'Int64', 'age':'Int64'})

count_employees(employees)
