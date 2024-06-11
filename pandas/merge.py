import pd as pd

data = [[1, 'Wang', 'Allen'], [2, 'Alice', 'Bob']]
person = pd.DataFrame(data,
                      columns=['personId', 'firstName', 'lastName'])\
    .astype({'personId': 'Int64', 'firstName': 'object', 'lastName': 'object'})

data = [[1, 2, 'New York City', 'New York'], [2, 3, 'Leetcode', 'California']]
address = pd.DataFrame(data,
                       columns=['addressId', 'personId', 'city', 'state'])\
    .astype({'addressId': 'Int64', 'personId': 'Int64', 'city': 'object', 'state': 'object'})

# join方法
# idx = person.index
# person = person.set_index('personId')
# address = address.set_index('personId')
# person.join(address).loc[:, ['firstName', 'lastName', 'city', 'state']].set_index(idx)

# merge方法
res = person.merge(address, on='personId', how='left')[['firstName', 'lastName', 'city', 'state']]
print(res)

