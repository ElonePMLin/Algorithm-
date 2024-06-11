class Solution {
    public long totalCost(int[] costs, int k, int candidates) {
        int n = costs.length;
        long ans = 0;
        if (n - 2 * candidates < k) {
            Arrays.sort(costs);  // 数组排序
            for (int i = 0; i < k; i++) {
                ans += costs[i];
            }
            return ans;
        }

        PriorityQueue<Integer> pre = new PriorityQueue<>();  // 初始化优先队列 '()' 非常重要
        PriorityQueue<Integer> suf = new PriorityQueue<>();  //
        for (int i = 0; i < candidates; i++) {
            pre.offer(costs[i]);
            suf.offer(costs[n - i - 1]);
        }

        // 双指针
        int i = candidates;
        int j = n - candidates - 1;
        while (k-- > 0) {
            if (pre.peek() <= suf.peek()) {  // 获取第一个数据 .peek()
                ans += pre.poll();
                pre.offer(costs[i++]);
            } else {
                ans += suf.poll();
                suf.offer(costs[j--]);
            }
        }
        return ans;
    }
}