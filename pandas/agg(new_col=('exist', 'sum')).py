import pandas as pd


# 对null只能默认为0，不能保持null
def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    aggregate = {}
    for m in month:
        department[f'{m}_Revenue'] = department['revenue'].mask(department['month'] != m, None)
        aggregate[f'{m}_Revenue'] = (f'{m}_Revenue', 'sum')
        # pd.NA if list(x.values).count(pd.NA) == len(x) else x.sum()
    df = department.groupby(by='id', as_index=False, dropna=True).agg(**aggregate)
    # df = df.mask(df == 0, None)
    return df


# 简介的写法
def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return department.pivot(index='id', columns='month', values='revenue').reindex(columns=month).rename(columns=lambda x: f'{x}_Revenue').reset_index()


data = [[1, 8000, 'Jan'], [2, 9000, 'Jan'], [3, 10000, 'Feb'], [1, 7000, 'Feb'], [1, 6000, 'Mar']]
department = pd.DataFrame(data, columns=['id', 'revenue', 'month']).astype({'id':'Int64', 'revenue':'Int64', 'month':'object'})

reformat_table(department)
