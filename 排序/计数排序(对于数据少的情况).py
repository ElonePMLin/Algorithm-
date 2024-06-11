from typing import List


# 计数排序
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        m = max(heights)
        cnt = [0] * (m + 1)

        for h in heights:
            cnt[h] += 1  # 统计指定高度数量（用于计算指定高度应该在哪个索引）

        idx = ans = 0
        for i in range(1, m + 1):
            for j in range(cnt[i]):
                if heights[idx] != i:  # idx索引的值 是否为 对应高度
                    ans += 1
                idx += 1
        return ans
