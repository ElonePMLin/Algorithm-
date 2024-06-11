# 节点移除后，仍能被其他节点的病毒感染
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        st = set(initial)
        vis = [False] * len(graph)
        def dfs(i):
            vis[i] = True

            nonlocal node, size

            # 状态更新
            if node != -2 and i in st:
                node = i if node == -1 else -2
            size += 1
            for j, link in enumerate(graph[i]):  # 对于节点i来说，能连接的节点
                if link and not vis[j]:  # 1 代表能被感染，且未被访问过
                    dfs(j)

            return

        ans = -1  # 需要移除的节点
        max_size = 0  # 当size相同的时候，取node最小的ans

        # 遍历病毒的位置
        for i in initial:
            if vis[i]:
                continue
            size = 0
            node = -1
            dfs(i)
            if node >= 0 and (size > max_size or size == max_size and ans > node):
                ans = node
                max_size = size
        return min(initial) if ans < 0 else ans
