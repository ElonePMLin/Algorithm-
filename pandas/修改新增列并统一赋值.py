import pandas as pd


def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    df = (triangle['x'] + triangle['y'] > triangle['z']) & (triangle['x'] + triangle['z'] > triangle['y']) & (triangle['z'] + triangle['y'] > triangle['x'])
    y = triangle[df]
    y['triangle'] = 'Yes'
    n = triangle[~df]
    n['triangle'] = 'No'
    return pd.concat([y, n])


data = [[13, 15, 30], [10, 20, 15]]
triangle = pd.DataFrame(data, columns=['x', 'y', 'z']).astype({'x':'Int64', 'y':'Int64', 'z':'Int64'})
