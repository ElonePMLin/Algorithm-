import pandas as pd


def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer.groupby(by='visited_on')['amount'].sum().reset_index()
    data = {
        'visited_on': [],
        'amount': [],
        'average_amount': []
    }
    for i in range(6, len(df)):
        data['visited_on'].append(df['visited_on'][i])
        data['amount'].append(df[i - 6: i + 1]['amount'].sum())
        data['average_amount'].append(round(df[i - 6: i + 1]['amount'].sum() / 7, 2))
    return pd.DataFrame(data)


data = [[1, 'Jhon', '2019-01-01', 100], [2, 'Daniel', '2019-01-02', 110], [3, 'Jade', '2019-01-03', 120], [4, 'Khaled', '2019-01-04', 130], [5, 'Winston', '2019-01-05', 110], [6, 'Elvis', '2019-01-06', 140], [7, 'Anna', '2019-01-07', 150], [8, 'Maria', '2019-01-08', 80], [9, 'Jaze', '2019-01-09', 110], [1, 'Jhon', '2019-01-10', 130], [3, 'Jade', '2019-01-10', 150]]
customer = pd.DataFrame(data, columns=['customer_id', 'name', 'visited_on', 'amount']).astype({'customer_id':'Int64', 'name':'object', 'visited_on':'datetime64[ns]', 'amount':'Int64'})

restaurant_growth(customer)


# 移动窗口版
def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer.groupby(by='visited_on')['amount'].sum().reset_index()
    df['average_amount'] = df['amount'].rolling(7).mean().round(2)
    df['amount'] = df['amount'].rolling(7).sum()
    return df[~df['amount'].isna()]


data = [[1, 'Jhon', '2019-01-01', 100], [2, 'Daniel', '2019-01-02', 110], [3, 'Jade', '2019-01-03', 120], [4, 'Khaled', '2019-01-04', 130], [5, 'Winston', '2019-01-05', 110], [6, 'Elvis', '2019-01-06', 140], [7, 'Anna', '2019-01-07', 150], [8, 'Maria', '2019-01-08', 80], [9, 'Jaze', '2019-01-09', 110], [1, 'Jhon', '2019-01-10', 130], [3, 'Jade', '2019-01-10', 150]]
customer = pd.DataFrame(data, columns=['customer_id', 'name', 'visited_on', 'amount']).astype({'customer_id':'Int64', 'name':'object', 'visited_on':'datetime64[ns]', 'amount':'Int64'})

print(restaurant_growth(customer))

