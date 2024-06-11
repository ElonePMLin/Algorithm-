import pandas as pd


def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:

    df = stadium[(stadium['people'] >= 100)]
    return df[
        (df['id'].isin(df['id'] + 1) & df['id'].isin(df['id'] + 2)) |
        (df['id'].isin(df['id'] + 1) & df['id'].isin(df['id'] - 1)) |
        (df['id'].isin(df['id'] - 1) & df['id'].isin(df['id'] - 2))
    ]
    # print(df['id'].isin(df['id'] - 1))
    # print(df['id'] - 1)
    # print(df['id'] - 2)
    # return stadium['id']


data = [[1, '2017-01-01', 10], [2, '2017-01-02', 109], [3, '2017-01-03', 150], [4, '2017-01-04', 99], [5, '2017-01-05', 145], [6, '2017-01-06', 1455], [7, '2017-01-07', 199], [8, '2017-01-09', 188]]
stadium = pd.DataFrame(data, columns=['id', 'visit_date', 'people']).astype({'id':'Int64', 'visit_date':'datetime64[ns]', 'people':'Int64'})

human_traffic(stadium)
