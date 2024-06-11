# 给定所需 列表大小k 和 总和大小n
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i, t):
            d = k - len(path)

            if t < 0 or t > (i * 2 - d + 1) * d // 2:  # 剪枝
                return

            if d == 0:
                ans.append(path.copy())
                return

                # 不选
            if i > d:
                dfs(i - 1, t)

            # 选
            path.append(i)
            dfs(i - 1, t - i)
            path.pop()

        dfs(9, n)
        return ans

