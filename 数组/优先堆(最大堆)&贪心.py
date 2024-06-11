from heapq import heapify, heapreplace
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # 210 / 2 = 105
        # 如何计算工资，什么情况下付出工资最少，性价比高
        # 假设 i 号员工，工作质量为 qi =  q[i]，工资为 wi = w[i]
        # 付出总钱计算方式：total = (qi + ... q) * wi / qi
        # 而 ri <= r，只要乘以最大的 工资质量比 则其他的 肯定能获取比期望值大的工资
        pairs = sorted(zip(quality, wage), key=lambda p: p[1] / p[0])
        h = [-q for q, _ in pairs[:k]]  # 最大堆，为了将quality更新为更小
        heapify(h)
        q_sum = -sum(h)
        res = q_sum * pairs[k - 1][1] / pairs[k - 1][0]  # 选最大的，以至于小的达到期望值
        for q, w in pairs[k:]:
            if -h[0] > q:
                q_sum += heapreplace(h, -q) + q
                res = min(res, q_sum * w / q)
        return res


Solution().mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2)
