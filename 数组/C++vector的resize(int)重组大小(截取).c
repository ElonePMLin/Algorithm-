class Solution {
public:
    vector<int> mostCompetitive(vector<int>& nums, int k) {
        int m = 0, n = nums.size();
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            // m + n - i > k 巧妙的设计 使后面的元素总是满足k个数据
            // [m]...[n] - i === 不要前i个，后面够k个的情况
            while (m > 0 && nums[m - 1] > x && m + n - i > k) {
                m--;
            }
            if (m < k) {
                nums[m++] = x;
            }
        }

        nums.resize(m);
        return nums;
        // return vector<int>(nums.begin(), nums.begin() + m); 效果一样
    }
};