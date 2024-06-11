class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # 相同值异或，偶数为0，基数为原值
        # 已知 4i ⊕ (4i + 1) ⊕ (4i + 2) ⊕ (4i + 3) = 0，连续四个整数异或为 0
        def sumXor(x: int):
            if x % 4 == 0:
                return x
            if x % 4 == 1:
                return 1
            if x % 4 == 2:
                return x + 1
            return 0

        # (start + i << 1)使start低位总是与start本身有关，则可以单独计算 => (new_start + i) << 1 + 低位
        e = start & n & 1  # n 为基 低位1，偶 低位0；& 1 取低位
        start >>= 1
        # start - 1为偏移，统计n个xor的结果
        return (sumXor(start - 1) ^ sumXor(start + n - 1)) << 1 | e
