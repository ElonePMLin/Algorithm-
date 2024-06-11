class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        n = len(arr)
        nums = [0] * 1001
        for j in range(n):
            for z in range(j + 1, n):
                if abs(arr[j] - arr[z]) <= b:
                    # 寻找满足数值范围的总个数
                    lj, rj = arr[j] - a, arr[j] + a
                    lk, rk = arr[z] - c, arr[z] + c
                    l = max(0, lj, lk)
                    r = min(1000, rj, rk)
                    if l <= r:
                        ans += nums[r] if l == 0 else nums[r] - nums[l - 1]
            # 数值更新，可以优化（数据量大的时候使用 离散化 或者 树状数组）
            for z in range(arr[j], 1001):
                nums[z] += 1
        return ans
