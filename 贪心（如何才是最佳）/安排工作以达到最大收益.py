from typing import List


# 可以重复选择任务，以便收益最大
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n, m = len(difficulty), len(worker)
        mp = sorted(zip(profit, difficulty), key=lambda x : -x[0])
        worker.sort(reverse=True)
        idx = 0
        ans = 0
        for w in worker:
            # 贪心思想，
            while idx < n and mp[idx][1] > w:
                idx += 1
            if idx < n:
                ans += mp[idx][0]
        return ans

    def maxProfitAssignment1(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        mp = sorted(zip(difficulty, profit))
        worker.sort()
        idx = 0
        ans = 0
        maxProfix = 0
        for w in worker:
            # 贪心思想，在符合要求的难度内选择最大收益，mp和worker都是按照 工作难度 从小到大排序，因此 idx 指针是界，避免多次计算最大值
            while idx < n and mp[idx][0] <= w:
                maxProfix = max(maxProfix, mp[idx][1])
                idx += 1
            ans += maxProfix
        return ans


difficulty = [2, 4, 6, 8, 10]
profit = [10, 20, 30, 40, 50]
worker = [4, 5, 6, 7]
# 100
print(Solution().maxProfitAssignment1(difficulty, profit, worker))

