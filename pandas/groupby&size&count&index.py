import pandas as pd


data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # for i in (person.groupby(by='email').count() > 1).loc[:'id']:
    #     print(i)
    # .size() 和 .count 类似
    df = person.groupby(by='email').size().reset_index(name="count")  # .reset_index(name="count") 重置索引 将原索引 还原到列中

    # print(df["count"] > 1)

    # df.index = ['yi', 'er']  # 索引序列与index没关系
    # print(df[[True, False]])  # df[[...]]  [...] 布尔值，返回为True的index，False的index不返回

    # print(df[df["count"] > 1][['email']])  # 两者不同，带多个 [] 能显示列索引
    # print(df[df["count"] > 1]['email'])  # 两者不同，少个 [] 只有数据没有列索引名
    print(df)
    p = person.groupby(by='email').count()
    # for i in range(len(p.index)):
    #     if p.iloc[i].values > 1:
    #         print(p.index[i])
    return pd.DataFrame([p.index[i] for i in range(len(p.index)) if p.iloc[i].values > 1], columns=['Email'])


print(duplicate_emails(person))


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person.groupby("email").size().reset_index(name="count")
    return df[df["count"] > 1][["email"]]

