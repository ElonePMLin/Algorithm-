class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        // 初始化字典
        unordered_map<string, int> mp = {{"type", 0}, {"color", 1}, {"name", 2}};
        int ans = 0, idx = mp[ruleKey];
        for (auto& item : items) {
            if (item[idx] == ruleValue) {
                ans++;
            }
        }
        return ans;
    }
};
