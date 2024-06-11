# 利用分桶思想(链地址法) 设计哈希映射
class MyHashMap:

    def __init__(self):
        self.hashMap = defaultdict(dict)
        self.size = 729

    def put(self, key: int, value: int) -> None:
        bucket = key % self.size
        self.hashMap[bucket][key] = value

    def get(self, key: int) -> int:
        bucket = key % self.size
        return self.hashMap[bucket].get(key, -1)

    def remove(self, key: int) -> None:
        bucket = key % self.size
        if self.hashMap[bucket].get(key, None):
            del self.hashMap[bucket][key]

