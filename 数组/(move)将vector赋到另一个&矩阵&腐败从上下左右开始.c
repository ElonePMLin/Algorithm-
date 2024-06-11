// q.push_back(make_pair(i, j))  ✅
// q.push_back(i, j)  ❌
// q.emplace_back(i, j)  ✅
// q.emplace_back(make_pair(i, j))  ✅

class Solution {
    int OFFSETDIS[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int fresh = 0;
        vector<pair<int, int>> q;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    q.push_back(make_pair(i, j));
                } else if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }

        int ans = -1;
        while (!q.empty()) {
            ans++;
            vector<pair<int, int>> nq;
            for (auto& [x, y] : q) {
                for (auto dis : OFFSETDIS) {
                    int nx = x + dis[0], ny = y + dis[1];
                    if (0 <= nx && nx < m && 0 <= ny && ny < n && grid[nx][ny] == 1) {
                        fresh--;
                        grid[nx][ny] = 2;
                        nq.push_back(make_pair(nx, ny));
                    }
                }
            }
            q = move(nq);  // np 赋值给 q
        }
        return fresh ? -1 : max(0, ans);
    }
};