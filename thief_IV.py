from bisect import bisect_left


class Solution:
    def minCapability(self, nums: [int], k: int) -> int:
        l, r = 0, max(nums)  # 从能偷0元，最大能偷max(nums)
        while l < r:
            mid = l + ((r - l) >> 1)
            if self.maxRoom(nums, mid, k):  # 房间多了
                r = mid
            else:
                l = mid + 1
        return l

    def maxRoom(self, nums, mx, k):  # 偷不大于mx钱时，最多需要偷多少间
        f0, f1 = 0, 0
        for x in nums:
            if x > mx:
                f0 = f1
            else:
                f0, f1 = f1, max(f1, f0 + 1)
        return f1 >= k


obj = Solution()
print(obj.minCapability([2,3,5,9], 2))
