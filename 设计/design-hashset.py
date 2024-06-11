# 利用分桶思想(链地址法) 设计哈希集合
from collections import defaultdict


class MyHashSet:

    def __init__(self):
        self.hset = defaultdict(set)
        self.size = 729

    def add(self, key: int) -> None:
        bucket = key % self.size
        self.hset[bucket].add(key)

    def remove(self, key: int) -> None:
        bucket = key % self.size
        if key in self.hset[bucket]:
            self.hset[bucket].remove(key)
        return

    def contains(self, key: int) -> bool:
        bucket = key % self.size
        if key in self.hset[bucket]:
            return True
        return False