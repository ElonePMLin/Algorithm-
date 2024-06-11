# k = n // m，k为最高倍数
# 等差数列 enable = m + 2m + 3m + ... + km = k(k + 1) / 2 * m。可以被整除
# 不能被整除，unable = 1 + 2 + ... + n - enable
# ans = unable - enable = 1 + 2 + ... + n - 2 * enable


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return n * (n + 1) // 2 - (n // m) * (n // m + 1) // 2 * m
