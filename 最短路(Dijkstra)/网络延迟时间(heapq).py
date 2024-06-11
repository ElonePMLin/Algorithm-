import heapq
from math import inf

times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]  # 有向节点 [from, to, times]
n = 4  # n个网络节点
k = 2  # 出发节点


# 最小堆方式
class Solution:
    def networkDelayTime(self, times, n, k):
        # Dijkstra
        # 建图
        graph = [[] for _ in range(n)]
        for frm, to, time in times:
            graph[frm - 1].append([to - 1, time])

        dis = [inf] * n
        dis[k - 1] = 0
        q = [(0, k - 1)]
        while q:
            time, frm = heapq.heappop(q)
            if dis[frm] < time:
                continue  # 通过frm节点有更短的路径
            for to, ti in graph[frm]:  # 从frm出发，连通graph[frm]节点
                if (nt := time + ti) < dis[to]:
                    dis[to] = nt  # 通过to的有更短路径
                    heapq.heappush(q, (nt, to))
        ans = max(dis)
        return ans


print(Solution().networkDelayTime(times, n, k))


# 传统Dijkstra算法
class Solution:
    def networkDelayTime(self, times, n, k):
        g = [[float('inf')] * n for _ in range(n)]
        for x, y, time in times:
            g[x - 1][y - 1] = time

        dist = [float('inf')] * n
        dist[k - 1] = 0
        used = [False] * n
        for _ in range(n):
            x = -1
            for y, u in enumerate(used):
                if not u and (x == -1 or dist[y] < dist[x]):  # 取路径最小的
                    x = y

            # 因为已经设了k - 1开始路径为 0，所以这里总是从 k - 1 开始
            used[x] = True

            for y, time in enumerate(g[x]):
                # 设置 y 为最短路径
                dist[y] = min(dist[y], dist[x] + time)

        ans = max(dist)
        return ans if ans < float('inf') else -1


print(Solution().networkDelayTime(times, n, k))
