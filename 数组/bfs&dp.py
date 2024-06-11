class Solution:
    def maxMoves(self, grid) -> int:
        # bfs
        m = len(grid)
        n = len(grid[0])
        q = [(i, 0) for i in range(m)]
        ans = 0
        while q:
            size = len(q)
            ans += 1
            for _ in range(size):
                row, col = q.pop()
                for r, c in [(-1, 1), (0, 1), (1, 1)]:
                    nr = row + r
                    nc = col + c
                    if 0 <= nr < m and 0 <= nc < n and grid[row][col] < grid[nr][nc]:
                        q.append((nr, nr))
        return ans

# 因此从题目出发解题：你可以从矩阵第一列中的 任一 单元格出发，按以下方式遍历 grid
# 且从单元格 (row, col)
#   可以移动到 (row - 1, col + 1)、(row, col + 1) 和 (row + 1, col + 1) 三个单元格中
#   任一满足值 严格 大于当前单元格的单元格。

# 每一格都是往前一列移动，所以可以从搜索列的方向出发，即 for c in range(n)
# 而每次都需要 与+1 比较，因此 for c in range(n-1) 确保不会 out of index
# 初始状态即为 q = range(m)

# 上述符合要求但执行会超出时间限制，用 set() 或者vis = range(m) 解决该问题
# 超时间的关键在于不遍历重复的元素

class Solution:
    def maxMoves(self, grid) -> int:
        # bfs
        m = len(grid)
        n = len(grid[0])
        q = set(range(m))
        for c in range(n - 1):
            tmp = set()
            for r in q:
                for nr in [r - 1, r, r + 1]:
                    if 0 <= nr < m and grid[r][c] < grid[nr][c + 1]:
                        tmp.add(nr)
            q = tmp
            if not q:
                return c
        return n - 1


# 空间优化（负数代表走过）
class Solution:
    def maxMoves(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        for row in grid:
            row[0] *= -1  # 入队标记
        for j in range(n - 1):
            for i, row in enumerate(grid):
                if row[j] > 0:  # 不在队列中
                    continue
                for k in i - 1, i, i + 1:
                    if 0 <= k < m and grid[k][j + 1] > -row[j]:
                        grid[k][j + 1] *= -1  # 入队标记
            if all(row[j + 1] > 0 for row in grid):  # 无法再往右走了
                return j
        return n - 1


