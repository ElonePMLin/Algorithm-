import pandas as pd


def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')

    # transactions['state'].apply(lambda x: 1 if x == 'approved' else 0)
    approval = transactions[transactions['state'] == 'approved'].groupby(by=['country', 'month'])
    trans = transactions.groupby(by=['country', 'month'])

    transactions['trans_count'] = trans['amount'].transform('count')
    # transactions['approved_count'] = approval['state'].transform('count')
    approved_count = approval['state'].count().reset_index(name='approved_count')
    transactions['trans_total_amount'] = trans['amount'].transform('sum')
    # transactions['approved_total_amount'] = approval['amount'].transform('sum')
    approved_total_amount = approval['amount'].sum().reset_index(name='approved_total_amount')
    df = approved_count.merge(approved_total_amount, on=['month', 'country'])
    print(df)
    # print(transactions.groupby(by=['country', 'month']).sample()[['month', 'country', 'trans_count', 'approved_count', 'trans_total_amount', 'approved_total_amount']].fillna(0))
    print(transactions.groupby(by=['country', 'month']).get_group())
    df1 = transactions.groupby(by=['country', 'month']).sample()
    return df1.merge(df, on=['month', 'country'], how='left')[['month', 'country', 'trans_count', 'approved_count', 'trans_total_amount', 'approved_total_amount']].fillna(0)


data = [[121, 'null', 'declined', 1000, '2018-12-18'], [122, 'US', 'declined', 2000, '2018-12-19'], [123, 'US', 'approved', 2000, '2019-01-01'], [124, 'DE', 'approved', 2000, '2019-01-07']]
transactions = pd.DataFrame(data, columns=['id', 'country', 'state', 'amount', 'trans_date']).astype({'id':'Int64', 'country':'object', 'state':'object', 'amount':'Int64', 'trans_date':'datetime64[ns]'})

print(monthly_transactions(transactions))
