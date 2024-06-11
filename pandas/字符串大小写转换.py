import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # users['name'] = users['name'].str.capitalize()  # 首字母大写
    users['name'] = users['name'].str.title()  # 首字母大写
    # users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()
    return users.sort_values(by='user_id', ascending=True)


data = [[1, 'aLice'], [2, 'bOB']]
users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})

print(fix_names(users))

