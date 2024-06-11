# 窗口大小固定的情况 size
# i - size + 1 >= 0  证明长度已经超过窗口大小，也能取到窗口最左的 index
List = list


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        s_a = [0, 0]
        max_anger = 0

        for i, (c, g) in enumerate(zip(customers, grumpy)):
            s_a[g] += c
            if i < minutes - 1:  # 窗口长度不足 minutes
                continue
            max_anger = max(max_anger, s_a[1])
            if grumpy[i - minutes + 1]:  # s_a[1] 满足 minutes 后，已经计算了最大值，将最左的一个元素去除
                s_a[1] -= customers[i - minutes + 1]

        return s_a[0] + max_anger
