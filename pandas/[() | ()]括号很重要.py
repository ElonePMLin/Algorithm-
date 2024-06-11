import pandas as pd


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    print(customer[customer['referee_id'].isna() | (customer['referee_id'] != 2)])
    # print(customer[customer['referee_id'].isna() | customer['referee_id'] != 2])  # 错误
    # print(customer['referee_id'] != 2)
    return customer[customer.fillna(0)['referee_id'] != 2][['name']]


data = [[1, 'Will', None], [2, 'Jane', None], [3, 'Alex', 2], [4, 'Bill', None], [5, 'Zack', 1], [6, 'Mark', 2]]
customer = pd.DataFrame(data, columns=['id', 'name', 'referee_id']).astype({'id':'Int64', 'name':'object', 'referee_id':'Int64'})

print(find_customer_referee(customer))
