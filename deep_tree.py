from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def lcaDeepestLeaves(self, root):
        def f(root):
            if not root:
                return 0, None

            d1, lca1 = f(root.left)
            d2, lca2 = f(root.right)

            if d1 > d2:
                return d1 + 1, lca1
            if d1 < d2:
                return d2 + 1, lca2
            return d1 + 1, root

        return f(root)[1]


def deserializer(serializer):
    serializer = deque(serializer)

    def dfs():
        if len(serializer) < 1:
            return
        val = serializer.popleft()
        if not val and val != 0:
            return None

        node = TreeNode(val)
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()


def serializer(tree):
    ans = []

    def dfs(node):
        if not node:
            return ans.append("")

        ans.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(tree)
    return ans


root = [3,5,6,'','',2,7,'','',4,'','',1,0,'','',8,'','']  # 应该用广度 反序列化 leetcode的


root = deserializer(root)
print(serializer(root))

res = Solution().lcaDeepestLeaves(root)
print(serializer(res))
