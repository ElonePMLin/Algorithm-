class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        has = set()
        ans = 0
        for w in words:
            if w[::-1] in has:
                ans += 1
            else:
                has.add(w)
        return ans

