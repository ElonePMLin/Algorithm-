import pandas as pd


def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['state'] = transactions['state'].apply(lambda x: 0 if x == 'declined' else 1)
    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')
    transactions['approved_total_amount'] = transactions['state'].mask(transactions['state'] == 1, transactions.amount)
    transactions['approved_count'] = transactions['state'].where(transactions['state'] != 1, 1)
    print(transactions)
    return transactions.groupby(by=['month', 'country'], dropna=False, as_index=False).agg({
        'state': 'count', 'approved_count': 'sum', 'amount': 'sum', 'approved_total_amount': 'sum'
    }).rename(columns={'state': 'trans_count', 'amount': 'trans_total_amount'})


data = [[121, 'null', 'declined', 1000, '2018-12-18'], [122, 'US', 'declined', 2000, '2018-12-19'], [123, 'US', 'approved', 2000, '2019-01-01'], [124, 'DE', 'approved', 2000, '2019-01-07']]
transactions = pd.DataFrame(data, columns=['id', 'country', 'state', 'amount', 'trans_date']).astype({'id':'Int64', 'country':'object', 'state':'object', 'amount':'Int64', 'trans_date':'datetime64[ns]'})

print(monthly_transactions(transactions))

