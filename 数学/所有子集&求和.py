from typing import List
# 给定数组，如[5, 1, 6]，找出所有子集并异或的值求和


# dfs方法，选或不选即可解决问题
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        def dfs(val, idx):
            nonlocal res
            if idx == n:
                # 终止递归
                res += val
                return
            # 考虑选择当前数字
            dfs(val ^ nums[idx], idx + 1)
            # 考虑不选择当前数字
            dfs(val, idx + 1)

        dfs(0, 0)
        return res


# 子集与元素
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(1 << n):  # 遍历所有子集，一个数组有 n 个元素，则子集有 (1 << n) - 1 个
            tmp = 0
            for j in range(n):  # 遍历每个元素
                #   n  =           0       1     2       3       4       5       6
                # 当 0 时，0000 & 00001  00010  空集
                # 当 1 时，0001 & 00001  01 10 11 100   [0]
                # 当 2 时，0010 & 00001  01 10 11 100   [1]
                # 当 3 时，0011 & 00001  01 10 11       [0, 1]
                # 当 7 时，0111 & 00001  01 10 11 100 101 110 111
                # 当 i.bit_count() % 2 != 0 即可计算计数个的子集（不是连续的）
                if i & (1 << j):
                    tmp ^= nums[j]
            res += tmp
        return res


# 统计每个1，在使其左移 n - 1
# 求总和，异或丢失的 0 总会被加回来。因此 统计所有1
# 相加 进位 << (n - 1)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for ns in nums:
            ans |= ns
        return ans << (n - 1)

# [1, 2]  -> [1] [2] [1, 2] -> 1 + 2 + 3 = 6 = 110
# 01 | 10 = 11 << (n - 1) = 110
# [2, 3]  -> [2]  [3]  [2, 3]  ->  2 + 3 + 1 = 6 = 110
#  10 | 11 = 11 << (n - 1) = 110
