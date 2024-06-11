// 空间优化
class Solution {
    public int maxMoves(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        for (int[] row : grid) {
            row[0] *= -1;
        }
        for (int c = 0; c < n - 1; c++) {
            boolean flag = false;
            for (int r = 0; r < m; r++) {
                if (grid[r][c] > 0) {
                    continue;
                }
                for (int nr = Math.max(r - 1, 0); nr < Math.min(r + 2, m); nr++) {
                    if (-grid[r][c] < grid[nr][c + 1]) {
                        grid[nr][c + 1] *= -1;
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
}

// bfs
// 显然 List<Integer> q = new ArrayList<>(m); 和 int[][] 不同；
// List<Integer> q = new ArrayList<>(m);  能执行增删？
// .add(); .isEmpty()
// int[][] 添加数据  Arrays.fill(vis, -1);
class Solution {
    public int maxMoves(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] vis = new int[m];
        Arrays.fill(vis, -1);
        List<Integer> q = new ArrayList<>(m);
        for (int i = 0; i < m; i++) {
            q.add(i);
        }
        for (int j = 0; j < n - 1; j++) {
            List<Integer> nxt = new ArrayList<>();
            for (int i : q) {
                for (int k = Math.max(i - 1, 0); k < Math.min(i + 2, m); k++) {
                    if (vis[k] != j && grid[k][j + 1] > grid[i][j]) {
                        vis[k] = j; // 第 k 行目前最右访问到了 j
                        nxt.add(k);
                    }
                }
            }
            if (nxt.isEmpty()) { // 无法再往右走了
                return j;
            }
            q = nxt;
        }
        return n - 1;
    }
}

