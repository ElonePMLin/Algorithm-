class Solution {
public:
    vector<int> distinctDifferenceArray(vector<int>& nums) {
        int n = nums.size();
        int suf[n + 1];  // 定义array
        suf[n] = 0;
        unordered_set<int> mp;
        for (int i = n - 1; i; i--) {
            mp.insert(nums[i]);
            suf[i] = mp.size();
        }

        mp.clear();
        vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            mp.insert(nums[i]);
            ans[i] = mp.size() - suf[i + 1];
        }
        return ans;
    }
};