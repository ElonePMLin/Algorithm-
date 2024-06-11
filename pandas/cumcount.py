import pandas as pd

data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
logs = pd.DataFrame(data, columns=['id', 'num']).astype({'id':'Int64', 'num':'Int64'})


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    def consecutive(data):
        cnt = 0
        idx = data.iloc[0, 0]
        for i in range(len(data)):
            if data.iloc[i, 0] - i == idx:
                cnt += 1
            else:
                if cnt >= 3:
                    return True
                else:
                    cnt = 1
                idx = data.iloc[i, 0] - i
        return cnt >= 3

    return pd.DataFrame({
        'ConsecutiveNums': logs.groupby(by='num').filter(consecutive).drop_duplicates(['num'])['num']
    })


import pandas as pd


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    # print(logs.groupby('num').cumcount())  # 分组并重新编号，为num分组并将值替换为编号，同组为相同编号
    # 计算每个数字的连续出现次数
    logs['consecutive'] = logs['id'] - (logs.groupby('num')['id'].cumcount()).astype(int)

    # 筛选出至少连续出现三次的数字
    # print(logs.groupby(['num', 'rnk_diff'])['id'].transform('count') >= 3)  # 取id列，count得出>=3的True/False
    result = logs[
        logs.groupby(['num', 'consecutive'])['id'].transform('count') >= 3
        ]['num'].drop_duplicates()

    # 返回结果，并将列命名为 ConsecutiveNums
    return result.to_frame(name='ConsecutiveNums')


print(consecutive_numbers(logs))

from collections import defaultdict
defaultdict()
