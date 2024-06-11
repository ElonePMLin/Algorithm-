// bfs
class Solution {
public:
    int maxMoves(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        for (auto &row : grid) {
            row[0] *= -1;  // 入队标记
        }
        for (int c = 0; c < n - 1; c++) {  // 从0列开始
            bool flag = false;
            for (int r = 0; r < m; r++) {
                if (grid[r][c] > 0) {
                    continue;
                }
                for (int nr = max(r - 1, 0); nr < min(r + 2, m); nr++) {  // 启;末;步
                    if (grid[nr][c + 1] > -grid[r][c]) {
                        grid[nr][c + 1] *= -1;  // 入队
                        flag = true;
                    }
                }
            }
            if (!flag) {
                return c;
            }
        }
        return n - 1;
    }
};

// dfs
class Solution {
public:
    int maxMoves(vector<vector<int>> &grid) {
        int m = grid.size(), n = grid[0].size();
        int ans = 0;
        function<void(int, int)> dfs = [&](int i, int j) {
            ans = max(ans, j);
            if (ans == n - 1) { // ans 已达到最大值
                return;
            }
            // 向右上/右/右下走一步
            for (int k = max(i - 1, 0); k < min(i + 2, m); k++) {  // 启;末;步
                if (grid[k][j + 1] > grid[i][j]) {
                    dfs(k, j + 1);
                }
            }
            grid[i][j] = 0;
        };
        for (int i = 0; i < m; i++) {
            dfs(i, 0); // 从第一列的任一单元格出发
        }
        return ans;
    }
};


// iota 函数是一个计算机语言中的函数，用于产生从val开始 「连续」 的值。[first, last)
// iota(q.begin(), q.end(), 0);  传入了q容器指针，修改了q容器的值
// 定义 vector .push_back(xx); .empty();
// q = move(nxt);  将nxt对象的内容 copy 到q中并覆盖
// vector<int> vis(m, -1);  默认生产m个-1
class Solution {
public:
    int maxMoves(vector<vector<int>> &grid) {
        int m = grid.size(), n = grid[0].size();
        vector<int> vis(m, -1), q(m);
        iota(q.begin(), q.end(), 0);  // iota 函数是一个计算机语言中的函数，用于产生连续的值。
        for (int j = 0; j < n - 1; j++) {
            vector<int> nxt;
            for (int i : q) {
                for (int k = max(i - 1, 0); k < min(i + 2, m); k++) {
                    if (vis[k] != j && grid[k][j + 1] > grid[i][j]) {
                        vis[k] = j; // 第 k 行目前最右访问到了 j
                        nxt.push_back(k);
                    }
                }
            }
            if (nxt.empty()) { // 无法再往右走了
                return j;
            }
            q = move(nxt);
        }
        return n - 1;
    }
};

