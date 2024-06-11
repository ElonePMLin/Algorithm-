import pd as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(['salary'])

    employee = employee.sort_values("salary", ascending=False)
    if len(employee['salary'].unique()) < 2:
        return pd.DataFrame({'SecondHighestSalary': [np.NaN]})
    else:
        return pd.DataFrame({'SecondHighestSalary': [employee['salary'].iloc[1]]})

# | id | salary |
# | -- | ------ |
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |

# 取第二高工资


# 取第N高工资
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(['salary'])
    employee = employee.sort_values('salary', ascending=False)
    if len(employee) >= N >= 1:
        return pd.DataFrame({f"getNthHighestSalary({N})": [employee['salary'].iloc[N-1]]})
    return pd.DataFrame({f"getNthHighestSalary({N})": [None]})


