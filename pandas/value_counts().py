import pandas as pd


def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # print(customer.groupby(by='customer_id').nunique())   # groupby下的 nunique() 代表 X 分组下，具有多少个不同数
    df = customer.groupby(by='customer_id')['product_key'].nunique().reset_index()
    return df[df['product_key'] == len(product)][['customer_id']]


data = [[1, 5], [2, 6], [3, 5], [3, 6], [1, 6]]
customer = pd.DataFrame(data, columns=['customer_id', 'product_key']).astype({'customer_id':'Int64', 'product_key':'Int64'})
data = [[5], [6]]
product = pd.DataFrame(data, columns=['product_key']).astype({'product_key':'Int64'})

print(find_customers(customer, product))
