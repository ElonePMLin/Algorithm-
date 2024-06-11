# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        cur = root.val
        if cur < low:
            return self.rangeSumBST(root.right, low, high)
        elif cur > high:
            return self.rangeSumBST(root.left, low, high)
        return cur + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)

