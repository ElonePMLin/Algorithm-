import pandas as pd


def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # pivot 以id为行索引，以month列数据为列索引，值为revenue 重塑表
    # .reindex(columns=['', '', ...])  修改列索引
    # .rename(columns=lambda x: f'{x}_Revenue')  格式化为正确的列名
    # .reset_index()  将id从行索引中放回数据中
    return department.pivot(index='id', columns='month', values='revenue').reindex(columns=month).rename(columns=lambda x: f'{x}_Revenue').reset_index()


data = [[1, 8000, 'Jan'], [2, 9000, 'Jan'], [3, 10000, 'Feb'], [1, 7000, 'Feb'], [1, 6000, 'Mar']]
department = pd.DataFrame(data, columns=['id', 'revenue', 'month']).astype({'id':'Int64', 'revenue':'Int64', 'month':'object'})

print(reformat_table(department))
