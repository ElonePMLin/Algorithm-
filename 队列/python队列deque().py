from collections import deque


class RecentCounter:

    def __init__(self):
        self.count = deque([])

    def ping(self, t: int) -> int:
        self.count.append(t)
        while self.count[0] < t - 3000:
            self.count.popleft()
        return len(self.count)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
