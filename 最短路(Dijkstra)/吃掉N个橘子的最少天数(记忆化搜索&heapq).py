# 题目分析
# 吃橘子的方式：
# 1、吃一个
# 2、剩余 n 橘子能被2整除，可以吃掉 n / 2 个
# 3、剩余 n 橘子能被3整除，可以吃掉 2 * (n / 3) 个

# 求最少天数，总是吃最多的
# 记忆化搜索（记忆化搜索：用一个哈希表 memo 记录 i 及其 dfs(i)，再次递归调用 dfs(i) 时，就可以直接返回 memo 中保存的数据了。Python 用户可以直接使用 @cache。）
# 设计输入 n 个橘子，输出 ans 天的 dfs(i) 记忆化搜索
# 吃最多，总是吃 n // 2，2 * (n // 3) 个；吃完就剩 n // 2 和 n // 3
# 因为考虑能否被整除，因此 ans1 = dfs(n // 2) + n % 2 + 1; ans2 = dfs(n // 3) + n % 3 + 1；n % 2、n % 3为吃一个
# 求最小值即可
from functools import lru_cache
from collections import defaultdict
from math import inf
from heapq import heappop, heappush


class Solution:
    def minDays(self, n: int) -> int:
        # 类似爬楼梯？
        # 从0开始一直到n

        @lru_cache
        def dfs(i):
            if i <= 1:
                return i
            return min(dfs(i // 2) + i % 2, dfs(i // 3) + i % 3) + 1
        return dfs(n)


print(Solution().minDays(10))


#
class Solution:
    def minDays(self, n: int) -> int:
        dis = defaultdict(lambda: inf)
        h = [(0, n)]
        while True:
            dx, x = heappop(h)
            if x <= 1:
                return dx + x
            if dx > dis[x]:  # 更大的天数，不使用
                continue
            for d in 2, 3:
                y = x // d  # 剩下多少橘子
                dy = dx + x % d + 1  # 吃了多少天
                if dy < dis[y]:  # y个橘子，有更小的天数，更新
                    dis[y] = dy
                    heappush(h, (dy, y))
