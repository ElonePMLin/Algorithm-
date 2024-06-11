class Solution {
public:
    vector<int> findColumnWidth(vector<vector<int>>& grid) {
        int n = grid[0].size();
        vector<int> ans(n);

        for (int j = 0; j < n; j++) {
            int maxx = 0, minn = 0;

            for (auto& row : grid) {
                maxx = max(maxx, row[j]);
                minn = min(minn, row[j]);
            }

            int len = 1;
            // 第二个参数是 x > 0;第三个参数需要赋值的
            for (int x = max(maxx / 10, -minn); x; x /= 10) {
                len++;
            }
            ans[j] = len;
        }
        return ans;
    }
};