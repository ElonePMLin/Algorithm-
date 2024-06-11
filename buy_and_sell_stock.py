class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        b1 = b2 = -prices[0]
        s1 = s2 = 0
        for i in range(1, n):
            b1 = max(b1, -prices[i])  # 总是买价格小的，取不到价格大的
            s1 = max(s1, b1 + prices[i])  # 当价格大时，能重新计算得到profit；价格小时，使用旧的profit
            b2 = max(b2, s1 - prices[i])  # 保存第一次购买的最大profit值
            s2 = max(s2, b2 + prices[i])  # 加上第二次购买的profit或者保存第一次最大的profit值
        return s2

obj = Solution()
print(obj.maxProfit([3,3,5,4,0,3,1,4]))
