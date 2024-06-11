from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        ans = mask = 0
        high_bit = nums[-1].bit_length() - 1
        for i in range(high_bit, -1, -1):  # 从最高位开始枚举
            mask |= 1 << i
            new_ans = ans | (1 << i)  # 这个比特位可以是 1 吗？
            d = {}
            for y in nums:
                mask_y = y & mask  # 低于 i 的比特位置为 0（为了比较前 i 的xor情况）

                # new_ans ^ mask_y （new_ans假设 第i位 为1）寻找 前i位 满足使 第 i 位为 1 的值
                # mask_y 保存 前i位 1 的 情况，当 new_ans ^ mask_y 时，能找到 某个值 i 位不同的情况，则可以更新ans
                if new_ans ^ mask_y in d and d[new_ans ^ mask_y] * 2 >= y:
                    ans = new_ans  # 这个比特位可以是 1
                    break
                d[mask_y] = y
        return ans
