class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0 or n == 1:
            return str(n)
        res = []
        while n:
            remainder = n & 1
            res.append(str(remainder))
            # n -= remainder
            # n //= -2
            n = -(n // 2)  # n = -(n >> 1)
        return ''.join(res[::-1])


# 计算机负数以补码的形式表示
# 给你一个整数 n ，以二进制字符串的形式返回该整数的 负二进制（base -2）表示。
# n = (-2)^(x+2) + (-2)^(x+1) + (-2)^x ...
# -(n >> 1) or -(n // 2) 当 最右 = 1，则取 1，最右 != 1，则取 0
