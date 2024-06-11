class SnapshotArray {
    private int snap_id = 0;

    private final Map<Integer, List<int[]>> snap_hist = new HashMap<>();

    public SnapshotArray(int length) {
    }

    public void set(int index, int val) {
        // 如果不存在，则添加
        // List<int[]> == ArrayList<>()
        //      .add(new int[]{snap_id, val})
        //      .get(index)  这是取索引的值
        //      .size()

        snap_hist.computeIfAbsent(index, key -> new ArrayList<>())  // 这里获取的便是ArrayList
            .add(new int[]{snap_id, val});
    }

    public int snap() {
        return snap_id++;
    }

    public int get(int index, int snap_id) {
        // Map
        //     .computeIfAbsent(K key, Function remappingFunction)
        //     .containsKey(index)
        //     .get(index)  // 这是取key的值
        if (!snap_hist.containsKey(index)) {
            return 0;
        }

        List<int[]> h = snap_hist.get(index);
        int j = bisect_search(h, snap_id);
        return j < 0 ? 0 : h.get(j)[1];
    }

    // left = -1; 的二分方法
    public int bisect_search(List<int[]> h, int goal) {
        int left = -1;
        int right = h.size();
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (h.get(mid)[0] <= goal) {
                left = mid;
            } else {
                right = mid;
            }
        }

        // 如果不存在，则 left 为其初始值 -1
        return left;
    }

    // left = 0; 的二分方法
    public int bisect(int[][] jobs, int right, int upper) {
        int left = 0;
        while (left < right) {
            int middle = (right + left) >>> 1;
            if (jobs[middle][0] <= upper) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        return left;
    }

}