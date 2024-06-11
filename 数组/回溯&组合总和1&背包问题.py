# 给定随机数字的数组，从中取值
# 回溯
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i, t):

            if t == 0:
                ans.append(path.copy())
                return

            if i == len(candidates) or t < candidates[i]:
                return

            # 不选
            dfs(i + 1, t)

            # 选
            path.append(candidates[i])
            dfs(i, t - candidates[i])
            path.pop()

        dfs(0, target)
        return ans


# 背包问题
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        # 完全背包
        f = [[False] * (target + 1) for _ in range(n + 1)]
        f[0][0] = True
        for i, x in enumerate(candidates):
            for j in range(target + 1):
                f[i + 1][j] = f[i][j] or j >= x and f[i + 1][j - x]

        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left == 0:
                # 找到一个合法组合
                ans.append(path.copy())
                return

            # 无法用下标在 [0, i] 中的数字组合出 left
            if left < 0 or not f[i + 1][left]:
                return

            # 不选
            dfs(i - 1, left)

            # 选
            path.append(candidates[i])
            dfs(i, left - candidates[i])
            path.pop()

        # 倒着递归，这样参数符合 f 数组的定义
        dfs(n - 1, target)
        return ans
