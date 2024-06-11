import pandas as pd


def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    # request_accepted[['requester_id', 'accepter_id']]
    df = pd.concat([request_accepted[['requester_id']].rename(columns={'requester_id': 'id'}),
               request_accepted[['accepter_id']].rename(columns={'accepter_id': 'id'})])
    return df.value_counts().reset_index().rename(columns={'count': 'num'}).sort_values(by='num', ascending=False).loc[:0]
    # return df.groupby(by='id')[['id']].count().rename(columns={'id': 'num'}).sort_values(by='num', ascending=False).reset_index().loc[:0]


data = [[1, 2, '2016/06/03'], [1, 3, '2016/06/08'], [2, 3, '2016/06/08'], [3, 4, '2016/06/09']]
request_accepted = pd.DataFrame(data, columns=['requester_id', 'accepter_id', 'accept_date']).astype({'requester_id':'Int64', 'accepter_id':'Int64', 'accept_date':'datetime64[ns]'})

print(most_friends(request_accepted))
