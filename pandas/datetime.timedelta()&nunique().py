import pandas as pd
import datetime


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby(by='player_id')['event_date'].min().reset_index()
    df['event_date'] += datetime.timedelta(days=1)
    # return
    return pd.DataFrame(
        {
            'fraction': [round(len(activity.merge(df, left_on=['player_id', 'event_date'], right_on=['player_id', 'event_date']).index) / len(df.index), 2)]
        }

    )


data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-03-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]
activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})

gameplay_analysis(activity)


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # print(activity['player_id'].nunique())  # Return number of unique elements in the object.
    activity['continue_login'] = activity.groupby(by='player_id')['event_date'].transform('min') + datetime.timedelta(days=1)
    # print(activity[activity['event_date'] == activity['continue_login']]['player_id'].count())
    return pd.DataFrame({
        'fraction': [
            round(activity[activity['event_date'] == activity['continue_login']]['player_id'].count()
                  / activity['player_id'].nunique(), 2)
        ]
    })


gameplay_analysis(activity)
