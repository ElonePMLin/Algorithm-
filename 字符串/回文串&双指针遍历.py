class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        for i in range(len(s) // 2):
            left, right = s[i], s[-1 - i]
            if left > right:  # 左边字典序大于右
                s[i] = right  # 左边的该为小的字典序
            else:
                s[-1 - i] = left
        return ''.join(s)

