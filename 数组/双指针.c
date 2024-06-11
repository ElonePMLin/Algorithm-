class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        ranges::sort(nums.begin(), nums.end());
        int n = nums.size();
        int ans = 0;
        for (int l = 0, r = n - 1; l < r; ) {
            if (nums[l] + nums[r] < target) {
                ans += r - l;
                l++;
            } else {
                r--;
            }
        }
        return ans;
    }
};