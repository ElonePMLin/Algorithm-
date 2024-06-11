class Solution {
    private static final int[][] OFFSETDIS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};  // 直接等于即可，不用 new int[4][2]{}

    public int orangesRotting(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int fresh = 0;
        List<int[]> q = new ArrayList<>();  // 不用Integer[]也可以，方便下面遍历写 int[]
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    q.add(new int[]{i, j});  // 赋值的时候[]内不填数字
                } else if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }

        int ans = -1;
        while (!q.isEmpty()) {
            ans++;
            List<int[]> nq = q;
            q = new ArrayList<>();
            for (int[] pos : nq) {
                for (int[] d : OFFSETDIS) {
                    int nx = pos[0] + d[0], ny = pos[1] + d[1];
                    if (0 <= nx && nx < m && 0 <= ny && ny < n && grid[nx][ny] == 1) {
                        fresh--;
                        grid[nx][ny] = 2;
                        q.add(new int[]{nx, ny});
                    }
                }
            }
        }
        return fresh != 0 ? -1 : Math.max(ans, 0);
    }
}