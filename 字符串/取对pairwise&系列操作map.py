from nltk import pairwise


class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(x - y) for x, y in pairwise(map(ord, s)))


print(Solution().scoreOfString('hello'))


class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i, j in zip(s[:], s[1:]):
            ans += abs(ord(i) - ord(j))
        return ans


Solution()
