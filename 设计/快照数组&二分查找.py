from collections import defaultdict
from bisect import bisect_left


# 最坏情况下，复制 50000 次长为 50000 的数组，会「超出内存限制」。
class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = 0
        self.snap_hist = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        self.snap_hist[index].append((self.snaps, val))

    def snap(self) -> int:
        self.snaps += 1
        return self.snaps - 1

    def get(self, index: int, snap_id: int) -> int:
        j = bisect_left(self.snap_hist[index], (snap_id + 1,)) - 1
        return self.snap_hist[index][j][1] if j >= 0 else 0


snap = SnapshotArray(12)
