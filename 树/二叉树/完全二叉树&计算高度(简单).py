# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 遍历到最后再计算
        leftLevel, rightLevel = 0, 0
        left, right = root.left, root.right
        while left:
            leftLevel += 1
            left = left.left
        while right:
            leftLevel += 1
            right = right.right
        if leftLevel == rightLevel:  # 都有左右节点的二叉树
            return (2 << leftLevel) - 1  #
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
