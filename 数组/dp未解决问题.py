# minimum-skips-to-arrive-at-meeting-on-time
# 准时抵达会议现场的最小跳过休息次数


class Solution:
    def minSkips(self, dist, speed: int, hoursBefore: int) -> int:
        # 脚程 * 总时间 = 最大路程，总路程 > 最大路程，肯定为 -1
        if sum(dist) > speed * hoursBefore:
            return -1
        dp = [0] * len(dist)

        for i in count(0):
            prev = 0
            for j, d in enumerate(dist[:-1]):
                tmp = dp[j + 1]
                dp[j + 1] = (dp[j] + d + speed - 1) // speed * speed
                if i:
                    dp[j + 1] = min(dp[j + 1], prev + d)
                prev = tmp
            if dp[-1] + dist[-1] <= speed * hoursBefore:
                return i


dist = [1,3,2]
speed = 4
hoursBefore = 2
# [7,3,5,5]
# 2
# 10
# [7,3,5,5]
# 1
# 10
# [2,4,4,9,10]
# 3
# 11
print(Solution().minSkips(dist, speed, hoursBefore))
