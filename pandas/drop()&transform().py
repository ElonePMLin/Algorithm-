import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # person['id'] != person.groupby(by='email')['id'].transform('min') 将所有ID变为最小，以便取出重复且id大的数据
    person.drop(
        person[person['id'] != person.groupby(by='email')['id'].transform('min')].index,
        inplace=True
    )
    print(person)


data = [[3, 'john@example.com'], [2, 'bob@example.com'], [1, 'john@example.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'int64', 'email':'object'})

delete_duplicate_emails(person)
