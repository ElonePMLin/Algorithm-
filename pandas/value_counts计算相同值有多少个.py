import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    num = employee['managerId'].value_counts()  # 可以计算出相同值的一共有多少个
    print(num)
    managers = num[num>=5].index  # 获取到managerId
    return employee.loc[employee['id'].isin(managers), ['name']]  # loc[xxx, ['name']] 获取到name列的数据


data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]
employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})

print(find_managers(employee))
