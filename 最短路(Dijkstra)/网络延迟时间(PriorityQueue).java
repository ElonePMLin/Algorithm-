class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        List<int[]>[] graph = new ArrayList[n];
        Arrays.setAll(graph, e -> new ArrayList<>());

        for (int[] val : times) {
            graph[val[0] - 1].add(new int[]{val[1] - 1, val[2]});
        }

        int maxDis = 0;
        int left = n; // 未确定最短路的节点个数
        int[] dis = new int[n];
        Arrays.fill(dis, Integer.MAX_VALUE);
        dis[k - 1] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> (a[0] - b[0]));  // a[0] - b[0] 比较方式
        pq.offer(new int[]{0, k - 1});  // 入堆
        while (!pq.isEmpty()) {
            int[] p = pq.poll();  // 退堆
            int time = p[0];
            int from = p[1];
            if (time > dis[from]) {
                continue;
            }

            maxDis = time;
            left--;
            for (int[] val : graph[from]) {
                int to = val[0];
                int nt = val[1] + time;
                if (nt < dis[to]) {
                    dis[to] = nt;
                    pq.offer(new int[]{nt, to});
                }
            }
        }
        return left == 0 ? maxDis : -1;
    }
}
