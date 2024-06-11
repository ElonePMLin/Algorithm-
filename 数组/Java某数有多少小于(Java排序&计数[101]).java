// 数据值最大为100
// 计数排序
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] cnt = new int[101];
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            cnt[nums[i]]++;  // 统计个数
        }

        // 求小于 i 的总数量
        for (int i = 1; i < 101; i++) {
            cnt[i] += cnt[i - 1];  // 小于等于 i 的数量有多少个
        }

        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = nums[i] == 0 ? 0 : cnt[nums[i] - 1];  // 计算小于 nums[i]（即nums[i] - 1）的数量
        }
        return ans;
    }
}


// 排序
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int n = nums.length;
        int[][] mp = new int[n][2];
        for (int i = 0; i < n; i++) {
            mp[i][0] = nums[i];
            mp[i][1] = i;
        }

        // Arrays.sort(mp, (i, j) -> i[0] - j[0]);
        Arrays.sort(mp, new Comparator<int[]>() {
            public int compare(int[] i, int[] j) {
                return i[0] - j[0];
            }
        });

        int[] ans = new int[n];
        int rank = -1;
        for (int i = 0; i < n; i++) {
            if (rank == -1 || mp[i][0] != mp[i - 1][0]) {
                rank = i;
            }
            ans[mp[i][1]] = rank;
        }
        return ans;
    }
}
