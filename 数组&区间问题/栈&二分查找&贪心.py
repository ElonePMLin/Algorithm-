from typing import List
from bisect import bisect_left


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1])
        # 栈中保存闭区间左右端点，栈底到栈顶的区间长度的和
        st = [(-2, -2, 0)]  # 哨兵，保证不和任何区间相交
        for start, end, d in tasks:
            _, r, s = st[bisect_left(st, (start,)) - 1]
            d -= st[-1][2] - s  # 去掉运行中的时间点，入栈的是总时间，所以 总时间 - s = 右边运行了多久时间，d -= 总时间 - s = 剩余多少时间没有运行
            if start <= r:  # start 在区间 st[i] 内
                d -= r - start + 1  # 去掉运行中的时间点  若区间重叠：减去已经运行的时间；否则：为原本运行时间
            if d <= 0:
                continue
            # 最小的 duration == 1
            while end - st[-1][1] <= d:  # 剩余的 d 填充区间后缀；若 结束时间 - 最后运行的时间 在剩余时间内
                l, r, _ = st.pop()
                d += r - l + 1  # 合并区间
            st.append((end - d + 1, end, st[-1][2] + d))
        return st[-1][2]


tasks = [[1, 3, 2], [2, 5, 3], [5, 6, 2], [3, 3, 1]]
Solution().findMinimumTime(tasks)
