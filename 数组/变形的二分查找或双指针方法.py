from bisect import bisect_left
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            find = target - nums[i]  # nums[x] < find
            ans += bisect_left(nums[i + 1:], find)
        return ans


Solution()


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        left, right = 0, n - 1
        while left < right:
            if nums[left] + nums[right] < target:
                ans += right - left
                left += 1
            else:
                right -= 1
        return ans


Solution()
