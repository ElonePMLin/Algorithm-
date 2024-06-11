from typing import List
from bisect import bisect_left


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))  # 按结束时间排序
        f = [0] * (len(jobs) + 1)
        for i, (_, st, p) in enumerate(jobs):
            j = bisect_left(jobs, (st + 1,), hi=i)  # f
            f[i + 1] = max(f[i], f[j] + p)  # f[i]，不选; f[j] + p 选
        return f[-1]
