# 组合总和 Ⅳ
# nums = [1,2,3], target = 4
# 类似于爬楼梯 nums为可以怎么爬，target为需要爬多少层

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        f = [1] + [0] * target
        for i in range(1, target + 1):
            f[i] = sum(f[i - x] for x in nums if x <= i)
        return f[target]


Solution().combinationSum4()