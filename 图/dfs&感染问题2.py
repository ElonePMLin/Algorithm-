# 连根拔起，移除后，不会被其他节点感染
# 该题是从遍历每个节点开始（除了感染源），从其他节点（A）遍历到感染节点（B），从而计算到A～B的感染数，累计最后得出最大的
# 该题当某个节点受两个感染源影响，则不统计该节点。
# 与感染问题1不同之处：
#   不是连根拔起
#   不从其他节点开始遍历，因为不是连根拔起，没必要统计当有两个感染源时其他节点受影响数，因为即使移除了该感染源，其他感染源仍会感染该移除的节点

from collections import Counter
from typing import List


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        st = set(initial)
        vis = [False] * len(graph)

        def dfs(i):
            vis[i] = True

            nonlocal size, node
            size += 1
            for j, link in enumerate(graph[i]):
                if not link:
                    continue

                if j in st:
                    # 遇到病毒源后，更新状态
                    if node != -2 and node != j:
                        node = j if node == -1 else -2
                elif not vis[j]:
                    dfs(j)
            return

        cnt = Counter()
        for i, seen in enumerate(vis):
            # 仅遍历未访问过的，且不是病毒源
            if seen or i in st:
                continue

            size = 0
            node = -1
            dfs(i)
            if node >= 0:
                cnt[node] += size

        # 使用max的缺点当size相同时，node会取最大值
        # 为了解决上述问题，使用min方法
        return min((-size, node) for node, size in cnt.items())[1] if cnt else min(initial)
    