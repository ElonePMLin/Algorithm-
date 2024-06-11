import pandas as pd


# 非常慢
def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    print(salary)
    for i, sex in enumerate(salary.loc[:, ['sex']].values):
        salary.loc[i, ['sex']] = 'm' if sex == 'f' else 'f'
    return salary


data = [[1, 'A', 'm', 2500], [2, 'B', 'f', 1500], [3, 'C', 'm', 5500], [4, 'D', 'f', 500]]
salary = pd.DataFrame(data, columns=['id', 'name', 'sex', 'salary']).astype({'id':'Int64', 'name':'object', 'sex':'object', 'salary':'Int64'})

print(swap_salary(salary))


# 快
def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex'] = salary['sex'].apply(lambda x:'f' if x=='m' else 'm')
    return salary


print(swap_salary(salary))
