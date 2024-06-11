import pandas as pd


def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    df = products[products['change_date'] <= '2019-08-16'].groupby(by='product_id')['change_date'].max().reset_index()
    df = products.merge(df, on='product_id', how='left')
    df = df[(df['change_date_x'] == df['change_date_y']) | df['change_date_y'].isna()]
    df.loc[df['change_date_y'].isna(), 'new_price'] = 10  # 取条件
    return df[['product_id', 'new_price']].rename(columns={'new_price': 'price'}).drop_duplicates()


data = [[1, 20, '2019-08-14'], [2, 50, '2019-08-14'], [1, 30, '2019-08-15'], [1, 35, '2019-08-16'], [2, 65, '2019-08-17'], [3, 20, '2019-08-18']]
products = pd.DataFrame(data, columns=['product_id', 'new_price', 'change_date']).astype({'product_id':'Int64', 'new_price':'Int64', 'change_date':'datetime64[ns]'})

price_at_given_date(products)
