// 分析看.py文件
class Solution {
    public long sellingWood(int m, int n, int[][] prices) {
        long[][] dp = new long[m + 1][n + 1];  // 定义数组，类型和大小
        for (int[] p : prices) {
            dp[p[0]][p[1]] = p[2];
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                for (int k = 1; k <= i / 2; k++) dp[i][j] = Math.max(dp[i][j], dp[k][j] + dp[i - k][j]);  // 水平
                for (int k = 1; k <= j / 2; k++) dp[i][j] = Math.max(dp[i][j], dp[i][k] + dp[i][j - k]);  // 垂直
            }
        }
        return dp[m][n];
    }
}

// Math.max(a, b)  获取最大值

// Map<Long, Integer> value = new HashMap<>();  // 定义字典
// 字典.put(key, val) 存放key, val;
// .containsKey(key)是否存在某key；.get(key)获取某key的值val

class Solution {
    public long sellingWood(int m, int n, int[][] prices) {
        Map<Long, Integer> value = new HashMap<>();  // 定义字典
        for (int[] price : prices) {
            value.put(pairHash(price[0], price[1]), price[2]); // 字典.put() 存放key, val
        }

        long[][] memo = new long[m + 1][n + 1];
        for (long[] row : memo) {
            Arrays.fill(row, -1);
        }
        return dfs(m, n, value, memo);
    }

    public long dfs(int x, int y, Map<Long, Integer> value, long[][] memo) {
        if (memo[x][y] != -1) {
            return memo[x][y];
        }

        long key = pairHash(x, y);
        long ret = value.containsKey(key) ? value.get(key) : 0;  // 字典.containsKey()是否存在某key；.get()获取某key的值
        if (x > 1) {
            for (int i = 1; i < x; i++) {
                ret = Math.max(ret, dfs(i, y, value, memo) + dfs(x - i, y, value, memo));
            }
        }
        if (y > 1) {
            for (int j = 1; j < y; j++) {
                ret = Math.max(ret, dfs(x, j, value, memo) + dfs(x, y - j, value, memo));
            }
        }
        memo[x][y] = ret;
        return ret;
    }

    public long pairHash(int x, int y) {
        return (long) x << 16 ^ y;
    }
}
