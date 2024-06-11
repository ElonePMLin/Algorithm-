# *grid 表示拆了grid的外皮[] ==> *grid = [1] [22] [333]
# zip() 内部可以传多个值(xx, yy, zz)
#       将每个值1、2、3、4... 一一对应 组成新元素


class Solution:
    def findColumnWidth(self, grid):
        ans = []
        for col in zip(*grid):
            x_len = 1
            x = max(max(col) // 10, -min(col))
            while x:
                x_len += 1
                x //= 10
            ans.append(x_len)
        return ans


grid = [[1], [22], [333]]
Solution().findColumnWidth(grid)

grid = [[-15, 1, 3], [15, 7, 12], [5, 6, -2]]
Solution().findColumnWidth(grid)
