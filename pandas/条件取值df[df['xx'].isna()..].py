import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    print(accounts[accounts['income'] < 20000]['income'].size)
    print(accounts[(20000 <= accounts['income']) & (accounts['income'] <= 50000)]['income'].size)
    print(accounts[(accounts['income'] > 50000)]['income'].size)
    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [
            accounts[accounts['income'] < 20000]['income'].size,
            accounts[(20000 <= accounts['income']) & (accounts['income'] <= 50000)]['income'].size,
            accounts[(accounts['income'] > 50000) | accounts['income'].isna()]['income'].size
        ]
    })


data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})

print(count_salary_categories(accounts))
