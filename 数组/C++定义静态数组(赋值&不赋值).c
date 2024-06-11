class Solution {
public:
    int oddCells(int m, int n, vector<vector<int>>& indices) {
        // int row[m];  静态数组，不赋值
        int* row = new int[m]{0};  // 静态数组，赋值为 0
        int* col = new int[n]{0};
        for (auto ind : indices) {
            row[ind[0]]++;
            col[ind[1]]++;
        }
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ans += (row[i] + col[j]) & 1;
            }
        }
        return ans;
    }
};