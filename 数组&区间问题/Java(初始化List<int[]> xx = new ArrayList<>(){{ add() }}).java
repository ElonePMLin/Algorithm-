class Solution {
    public int findMinimumTime(int[][] tasks) {
        Arrays.sort(tasks, (i, j) -> (i[1] - j[1]));
        // 初始化
        List<int[]> runned = new ArrayList<>() {{
            add(new int[]{-2, -2, 0});
        }};
        // 所有任务
        for (int[] t : tasks) {
            int n = runned.size();
            int start = t[0], end = t[1], duration = t[2];

            int[] before_runned = lower_bound(runned, start, n);
            int[] last_runned = runned.get(n - 1);

            duration -= last_runned[2] - before_runned[2];

            if (start <= before_runned[1]) {
                duration -= before_runned[1] - start + 1;
            }
            if (duration <= 0) continue;

            while (end - runned.get(runned.size() - 1)[1] <= duration) {
                last_runned = runned.remove(runned.size() - 1);  // 会返回删除的元素
                duration += last_runned[1] - last_runned[0] + 1;
            }
            runned.add(new int[]{end - duration + 1, end, duration + runned.get(runned.size() - 1)[2]});
        }

        return runned.get(runned.size() - 1)[2];
    }

    public int[] lower_bound(List<int[]> target, int val, int len) {
        int left = -1, right = len;
        while (left + 1 < right) {
            int mid = (right + left) / 2;
            if (target.get(mid)[0] <= val) {
                left = mid;
            } else {
                right = mid;
            }
        }
        return target.get(left);
    }
}