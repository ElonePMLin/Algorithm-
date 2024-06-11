class Solution {
public:
    vector<int> numberOfPairs(vector<int>& nums) {
        int pair = 0, n = nums.size();
        unordered_set<int> seen;
        for (auto num : nums) {
            if (seen.count(num)) {
                pair++;
                seen.erase(num);
            } else {
                seen.insert(num);
            }
        }
        return {pair, n - pair * 2};
    }
};