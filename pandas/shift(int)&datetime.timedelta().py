import pandas as pd
import datetime


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # 窗口函数更快
    # weather.sort_values('recordDate', inplace=True)
    # 利用窗口函数shift获取上一条数据的温度进行判断，此外我们还需要注意日期不连续的情况，所以需要再加一层判断，确保上一条数据日期为昨天。
    # res = weather[(weather['temperature'] > weather.shift(1)['temperature']) & (weather.shift(1)['recordDate'] == weather['recordDate'] - datetime.timedelta(days=1))]
    # return res[['id']]

    weather['tomorrow'] = weather['recordDate'] + datetime.timedelta(days=1)
    df = weather.merge(weather, left_on='tomorrow', right_on='recordDate')
    print(df[df['temperature_y'] - df['temperature_x'] > 0]['id_y'])


data = [[1, '2015-01-03', 10], [2, '2015-01-02', 25], [3, '2015-01-01', 20], [4, '2015-01-04', 30]]
weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})

print(rising_temperature(weather))
