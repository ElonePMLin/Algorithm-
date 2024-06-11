class Solution {
public:
    int maxDivScore(vector<int>& nums, vector<int>& divisors) {
        ranges::sort(nums, greater());  // 从大到小排序，也可以写成 ranges::greater
        int pairNum = 0, n = nums.size();
        for (int i = 1; i < n; i++) {
            pairNum += nums[i - 1] == nums[i] ? 1: 0;
        }
        ranges::sort(divisors);
        int maxCnt = -1, ans = 0;
        for (int d : divisors) {
            // ·
            if (maxCnt - pairNum >= nums[0] / d) {  // 贪心思想
                break;
            }
            int cnt = 0;
            for (int num : nums) {
                if (num < d) {
                    break;
                }
                cnt += num % d == 0 ? 1: 0;
            }
            if (maxCnt < cnt) {
                maxCnt = cnt;
                ans = d;
            }
        }
        return ans;
    }
};