import pandas as pd

data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})


# .isna() 返回布尔的数据，空值为True，非空为false
# 0    False
# 1     True
# 2    False
# 3     True
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    return df['customerId'].isna()


print(find_customers(customers, orders))


# 较快的方法
# ~代表 not in
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers.loc[~customers['id'].isin(orders['customerId'])][['name']].rename(columns={'name': 'Customers'})
