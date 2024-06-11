import pandas as pd


def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    root = tree[tree['p_id'].isna()]
    inner = tree[tree['id'].isin(tree['p_id']) & ~tree['p_id'].isna()]
    leaf = tree[~tree['id'].isin(tree['p_id']) & ~tree['p_id'].isna()]
    root.loc[:, 'p_id'] = 'Root'
    inner.loc[:, 'p_id'] = 'Inner'
    leaf.loc[:, 'p_id'] = 'Leaf'
    return pd.concat([root, inner, leaf]).rename(columns={'p_id': 'type'})


data = [[1, None], [2, 1], [3, 1], [4, 2], [5, 2]]
tree = pd.DataFrame(data, columns=['id', 'p_id']).astype({'id':'Int64', 'p_id':'Int64'})

print(tree_node(tree))
