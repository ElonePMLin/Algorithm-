class Solution {
public:
    vector<int> numberGame(vector<int>& nums) {
        ranges::sort(nums);
        int n = nums.size();
        for (int i = 0; i < n; i += 2) {
            swap(nums[i + 1], nums[i]);
        }
        return nums;
    }
};
