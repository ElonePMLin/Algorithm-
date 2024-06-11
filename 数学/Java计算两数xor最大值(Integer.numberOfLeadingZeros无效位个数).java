class Solution {
    public int maximumStrongPairXor(int[] nums) {
        Arrays.sort(nums);
        int highBit = 31 - Integer.numberOfLeadingZeros(nums[nums.length - 1]);

        int ans = 0, mask = 0;
        Map<Integer, Integer> mp = new HashMap<>();
        for (int i = highBit; i >= 0; i--) { // 从最高位开始枚举
            mp.clear();
            mask |= 1 << i;
            int newAns = ans | (1 << i); // 这个比特位可以是 1 吗？
            for (int y : nums) {
                int maskY = y & mask; // 低于 i 的比特位置为 0
                if (mp.containsKey(newAns ^ maskY) && mp.get(newAns ^ maskY) * 2 >= y) {
                    ans = newAns; // 这个比特位可以是 1
                    break;
                }
                mp.put(maskY, y);
            }
        }
        return ans;
    }
}
