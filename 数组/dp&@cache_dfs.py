# 给你两个整数 m 和 n ，分别表示一块矩形木块的高和宽。
# 同时给你一个二维整数数组 prices ，其中 prices[i] = [hi, wi, pricei]
# 表示你可以以 pricei 元的价格卖一块高为 hi 宽为 wi 的矩形木块。
#
# 每一次操作中，你必须按下述方式之一执行切割操作，以得到两块更小的矩形木块：
#
# 沿垂直方向按高度 完全 切割木块，或
# 沿水平方向按宽度 完全 切割木块
# 在将一块木块切成若干小木块后，你可以根据 prices 卖木块。
# 你可以卖多块同样尺寸的木块。你不需要将所有小木块都卖出去。你 不能 旋转切好后木块的高和宽。
#
# 请你返回切割一块大小为 m x n 的木块后，能得到的 最多 钱数。
#
# 注意你可以切割木块任意次。
# from functools import cache


class Solution:
    def sellingWood(self, m: int, n: int, prices) -> int:
        hashMap = {}

        # @cache  # 实现缓存
        def dfs(x: int, y: int) -> int:
            price = hashMap.get((x, y), 0)

            if x > 1:
                for z in range(1, x):
                    price = max(price, dfs(z, y) + dfs(x - z, y))

            if y > 1:
                for j in range(1, y):
                    price = max(price, dfs(x, j) + dfs(x, y - j))

            return price

        for i in prices:
            hashMap[(i[0], i[1])] = i[2]

        ans = dfs(m, n)
        # dfs.cache_clear()
        return ans


# 遍历所有切割方式，取到最大价格即可，由于数据量比较大，使用cache缓存数据
# 逐渐将切割扩大，边界为m, n;分别以高为界遍历所有切割方式取最大值，然后再以宽为界遍历所有切割方式取最大值
print(Solution().sellingWood(3, 5, [[1,4,2],[2,2,7],[2,1,3]]))

# 优化
# 实际上，横着切开，虽然位置不同，但得到的结果是相同的，
# 即一个高为 2 宽为 5 的木块，和一个高为 1 宽为 5 的木块，所以本质上只有 1 种切法。
# 对于竖切也同理，本质上只有 2 种切法。

# dp 也是同理，遍历所有切割方式
class Solution:
    def sellingWood(self, m: int, n: int, prices) -> int:
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for h, w, p in prices:
            dp[h][w] = p

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(
                    dp[i][j],
                    max((dp[k][j] + dp[i - k][j] for k in range(1, i // 2 + 1)), default=0),  # 水平
                    max((dp[i][k] + dp[i][j - k] for k in range(1, j // 2 + 1)), default=0)  # 垂直
                )
        return dp[m][n]

# 题目分析（寻找子问题、状态定义）
# 寻找子问题：一个高3 宽5 的木块，比如横着切分为一个高2 宽5，高1 宽5的木块，
#   接着竖着切，这意味着我们要处理的问题都是「高为 i 宽为 j 的木块」。
# 状态定义：
#   定义反映状态：dp[i][j] 为切割一块高 i 宽 j 的木块，能得到的最多钱数。
#   分类讨论：（如存在）则收益为price
#           （竖着切）每一刀都分割出不同宽度的木块（宽 k），即高 i 宽 k，或宽 j-k，最大收益为 max(遍历所有不同切法)
#           （横着切）每一刀都分割出不同高度的木块（高 k），即宽 j 高 k，或高 i-k，最大收益为 max(遍历所有不同切法)
#            最终到木块 高m，宽n，取上述3种最大值即为答案


