# 拓扑排序
class Solution:
    def findMinHeightTrees(self, n: int, edges):
        if n == 1:
            return [0]
        # 计算入度
        deg = [[] for _ in range(n)]
        indeg = [0] * n
        for i, j in edges:
            # 节点的子节点值（以便在下面验证节点）
            deg[i].append(j)
            deg[j].append(i)
            # 节点的子节点数量，即为度（以便验证节点是否为根节点，即是否还有子节点）
            indeg[i] += 1
            indeg[j] += 1

        # 开始遍历的数组（根节点）
        q = [i for i, d in enumerate(indeg) if d == 1]
        while n > 2:
            n -= len(q)  # 剩余节点数，获取最小高度树
            tmp = q
            q = []
            for node in tmp:
                for root in deg[node]:
                    indeg[root] -= 1
                    if indeg[root] == 1:
                        q.append(root)
        return q


# dfs
class Solution:
    def findMinHeightTrees(self, n: int, edges):
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n
        maxDepth, node = 0, -1

        def dfs(x: int, pa: int, depth: int):
            nonlocal maxDepth, node
            if depth > maxDepth:
                maxDepth, node = depth, x
            parents[x] = pa
            for y in g[x]:
                if y != pa:
                    dfs(y, x, depth + 1)
        dfs(0, -1, 1)  # 从 0 找到最远节点 node
        maxDepth = 0
        dfs(node, -1, 1)  # 从 node 找到最远节点 node2

        path = []
        while node != -1:  # 从 node2 节点开始往上找 node～node2 最长距离
            path.append(node)
            node = parents[node]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]


# bfs
from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges):
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n

        def bfs(start: int):
            vis = [False] * n
            vis[start] = True
            q = deque([start])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = True
                        parents[y] = x
                        q.append(y)
            return x
        x = bfs(0)  # 找到与节点 0 最远的节点 x
        y = bfs(x)  # 找到与节点 x 最远的节点 y

        path = []
        parents[x] = -1
        while y != -1:
            path.append(y)
            y = parents[y]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]

