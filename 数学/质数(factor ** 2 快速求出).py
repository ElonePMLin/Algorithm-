class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        for i in range(left, right + 1):
            num = i.bit_count()
            if num < 2:
                continue
            factor = 2
            flag = False
            while factor * factor <= num:
                if num % factor == 0:
                    flag = True
                    break
                factor += 1
            if not flag:
                ans += 1
        return ans

# 更快的方法
# right <= 10 ^ 6 < 2 ^ 20  19 位
# 2 <= x <= 19 的质数为 2，3，5，7，11，13，17，19
# mask = 10100010100010101100 == 665772
# 只需要 (1 << num.bit_count()) & mask != 0 即为答案
