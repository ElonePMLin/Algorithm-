from typing import List


class Node:
    # 该类实例只能创建__slots__中声明的属性，否则报错
    __slots__ = 'children', 'cnt'

    def __init__(self):
        self.children = [None, None]
        self.cnt = 0  # 子树大小


class Trie:
    HIGH_BIT = 6

    def __init__(self):
        self.root = Node()

    def insert(self, val):
        cur = self.root
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = (val >> i) & 1
            if cur.children[bit] is None:
                cur.children[bit] = Node()
            cur = cur.children[bit]
            cur.cnt += 1  # 维护子树大小
        return cur

    def remove(self, val):
        cur = self.root
        for i in range(Trie.HIGH_BIT, -1, -1):
            cur = cur.children[(val >> i) & 1]
            cur.cnt -= 1
        return cur

    def max_xor(self, val):
        cur = self.root
        ans = 0
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = (val >> i) & 1
            # xor，只有存在不同才是1
            if cur.children[bit ^ 1] and cur.children[bit ^ 1].cnt:
                ans |= 1 << i
                bit ^= 1
            cur = cur.children[bit]
        return ans


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        t = Trie()
        ans = left = 0
        for num in nums:
            t.insert(num)
            while 2 * nums[left] < num:
                t.remove(nums[left])
                left += 1

            ans = max(ans, t.max_xor(num))
        return ans
