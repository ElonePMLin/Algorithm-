class Solution:
    def longestAwesome(self, s: str) -> int:
        D = 10  # s 中的字符种类数
        n = len(s)
        pos = [n] * (1 << D)  # n 表示没有找到异或前缀和
        pos[0] = -1  # pre[-1] = 0
        ans = pre = 0
        for i, x in enumerate(map(int, s)):
            pre ^= 1 << x
            ans = max(ans, i - pos[pre],  # 偶数
                      max(i - pos[pre ^ (1 << d)] for d in range(D)))  # 奇数
            if pos[pre] == n:  # 首次遇到值为 pre 的前缀异或和，记录其下标 i
                pos[pre] = i
        return ans


s = '3242415'
# 遇到相同的数字(偶数个)，最终都抵消了，由于保存了前缀和的索引，因此能得到长度
# map ->
# 3 = 8 -> 0
# 32 = 12 -> 1
# 324 = 28 -> 2
# 3242 = 24 -> 3
# 32424 = 8 -> 4
# 324241 = 10 -> 5
# 3242415 = 42 -> 6
