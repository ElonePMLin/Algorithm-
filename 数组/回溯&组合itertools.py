# 给定所需 列表大小k 和 总和大小n
import itertools


# 利用迭代工具
# itertools.combinations(range(1, n + 1), k)  (list, num)
class Solution:
    def combine(self, n: int, k: int):
        # list = []
        # nums = [i+1 for i in range(n)]

        # import itertools
        return list(itertools.combinations(range(1, n + 1), k))


n, k = 4, 2
print(Solution().combine(n, k))


class Solution:
    def combine(self, n: int, k: int):
        ans = []
        path = []

        def dfs(i, k):
            d = k - len(path)
            if d == 0:
                ans.append(path.copy())
                return

            # 不选 len(path) + n - i >= k，总长度 + 剩余长度 >= 需要的长度 才有资格不选
            if i > d:
                dfs(i - 1, k)

            # 选
            path.append(i)
            dfs(i - 1, k)
            path.pop()

        dfs(n, k)
        return ans


n, k = 4, 2
print(Solution().combine(n, k))
