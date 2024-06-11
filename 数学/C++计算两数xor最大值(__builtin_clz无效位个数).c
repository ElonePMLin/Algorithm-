class Solution {
public:
    int maximumStrongPairXor(vector<int>& nums) {
        ranges::sort(nums);
        // 获取最后一个值，并获取最长位数
        int max_length = 31 - __builtin_clz(nums.back());

        int ans = 0, mask = 0;
        unordered_map<int, int> mp;
        for (int i = max_length; i >= 0; i--) {
            mp.clear();
            mask |= 1 << i;
            int pos_ans = ans | (1 << i);

            for (int num : nums) {
                int num_mask = num & mask;

                if (mp.count(num_mask ^ pos_ans) && mp[num_mask ^ pos_ans] * 2 >= num) {
                    ans = pos_ans;
                    break;
                }
                mp[num_mask] = num;
            }
        }
        return ans;
    }
};