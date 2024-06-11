import pandas as pd


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    # my_numbers['cnt'] = my_numbers.groupby(by='num')['num'].transform('count')
    # df = my_numbers[my_numbers['cnt'] == 1][['num']].sort_values(by='num', ascending=False)
    # return df.iloc[:1] if df.iloc[:1].values else pd.DataFrame({'num': [None]})

    df_once = my_numbers.drop_duplicates(subset=['num'], keep =False)
    return pd.DataFrame({'num': df_once.max()})


data = [[8], [8], [3], [3], [1], [4], [5], [6]]
my_numbers = pd.DataFrame(data, columns=['num']).astype({'num':'Int64'})

biggest_single_number(my_numbers)
