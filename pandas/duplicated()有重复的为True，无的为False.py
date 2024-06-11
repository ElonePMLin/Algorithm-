import pandas as pd


def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    insurance['tiv'] = insurance.groupby(by='tiv_2015')['tiv_2015'].transform('count')
    insurance['loca'] = insurance.groupby(by=['lat', 'lon'])['tiv_2015'].transform('count')
    return pd.DataFrame({
        'tiv_2016' : [
            insurance[(insurance['tiv'] > 1) & (insurance['loca'] == 1)]['tiv_2016'].sum().round(2)
        ]
    })


data = [[1, 10, 5, 10, 10], [2, 20, 20, 20, 20], [3, 10, 30, 20, 20], [4, 10, 40, 40, 40]]
insurance = pd.DataFrame(data, columns=['pid', 'tiv_2015', 'tiv_2016', 'lat', 'lon']).astype({'pid':'Int64', 'tiv_2015':'Float64', 'tiv_2016':'Float64', 'lat':'Float64', 'lon':'Float64'})


find_investments(insurance)


def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    cond1 = insurance['tiv_2015'].duplicated(keep=False)
    cond2 = ~insurance[['lat', 'lon']].duplicated(keep=False)
    _sum = insurance[cond1 & cond2]['tiv_2016'].sum()
    return pd.DataFrame({'tiv_2016': [round(_sum, 2)]})


find_investments(insurance)
