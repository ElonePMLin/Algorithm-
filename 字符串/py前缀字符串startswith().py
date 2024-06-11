class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for i in words:
            res += i.startswith(pref)
        return res
