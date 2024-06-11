class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        int n = quality.length;
        Integer[] idx = new Integer[n];
        Arrays.setAll(idx, i -> i);  // 设置值，i为索引值
        Arrays.sort(idx, (i, j) -> wage[i] * quality[j] - wage[j] * quality[i]);

        int q_sum = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);  // 默认为最小堆，b - a为最大堆
        for (int i = 0; i < k; i++) {
            pq.offer(quality[idx[i]]);
            q_sum += quality[idx[i]];
        }

        double res = q_sum * ((double) wage[idx[k - 1]] / quality[idx[k - 1]]);
        for (int i = k; i < n; i++) {
            int q = quality[idx[i]];
            if (pq.peek() > q) {
                q_sum -= pq.poll() - q;
                pq.offer(q);
                res = Math.min(res, q_sum * ((double) wage[idx[i]] / quality[idx[i]]));
            }
        }
        return res;
    }
}
