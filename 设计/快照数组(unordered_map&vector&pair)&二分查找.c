class SnapshotArray {
private:
    int snap_id = 0;
    unordered_map<int, vector<pair<int, int>>> snap_hist;

public:
    SnapshotArray(int length) {
    }

    void set(int index, int val) {
        // snap_hist[index].emplace_back(snap_id, val)
        snap_hist[index].emplace_back(make_pair(snap_id, val));
    }

    int snap() {
        return snap_id++;
    }

    int get(int index, int snap_id) {
        auto& bisect_list = snap_hist[index];

        // !!lower_bound/upperbound的返回值是一个地址值，若要得到目标元素的下标，直接减去数组首地址的值即可
        // 两种写法，(list, goal)、(list.begin(), list.end(), goal)
        // list.begin(), list.end()   实际是list的地址值，在这些范围内找goal
        int j = ranges::lower_bound(bisect_list, make_pair(snap_id + 1, 0)) - bisect_list.begin() - 1;
        return j >= 0 ? bisect_list[j].second : 0;

        // auto x = upper_bound(data[index].begin(), data[index].end(), pair{snap_id + 1, -1});
        // return x == data[index].begin() ? 0 : prev(x)->second;
        // prev是什么？
    }
};
