# mask |= 1 << (ord(al) - ord('a'))  # 将字节存放在对应位置上


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mask = 0
        for al in allowed:
            mask |= 1 << (ord(al) - ord('a'))

        ans = 0
        for word in words:
            w_mask = 0
            for w in word:
                w_mask |= 1 << (ord(w) - ord('a'))
            ans += (w_mask | mask) == mask
        return ans
