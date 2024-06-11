class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;
        int[][] jobs = new int[n][];
        for (int i = 0; i < n; i++) {
            jobs[i] = new int[]{endTime[i], startTime[i], profit[i]};
        }
        Arrays.sort(jobs, (i, j) -> i[0] - j[0]);  // 按结束时间排序，以便在start时间中寻找之前

        int[] f = new int[n + 1];
        for (int i = 0; i < n; i++) {
            int j = bisect1(jobs, i, jobs[i][1]);
            int j = bisect2(jobs, i, jobs[i][1] + 1);
            f[i + 1] = Math.max(f[i], f[j] + jobs[i][2]);
        }
        return f[n];
    }

    public int bisect1(int[][] jobs, int right, int upper) {
        int left = 0;
        while (left < right) {
            int middle = (right + left) >>> 1;
//             int middle = (right + left) >> 1;
            if (jobs[middle][0] <= upper) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        return left;
    }

    public int bisect2(int[][] jobs, int right, int upper) {
        int left = 0;
        while (left < right) {
            int middle = (right + left) >>> 1;
//             int middle = (right + left) >> 1;
            if (jobs[middle][0] < upper) {  // 因为 upper+1 了，所以不能等于
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        return left;
    }
}
