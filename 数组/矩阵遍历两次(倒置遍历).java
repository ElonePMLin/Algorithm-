class Solution {
    public int[] findColumnWidth(int[][] grid) {
        int n = grid[0].length;
        int[] ans = new int[n];

        for (int j = 0; j < n; j++) {
            int maxx = 0;
            int minn = 0;

            for (int[] row : grid) {
                maxx = Math.max(maxx, row[j]);
                minn = Math.min(minn, row[j]);
            }

            int len = 1;
            for (int x = Math.max(maxx / 10, -minn); x > 0; x /= 10) {
                len++;
            }
            ans[j] = len;
        }
        return ans;
    }
}