class Solution {
public:
    int networkDelayTime(vector<vector<int>> &times, int n, int k) {
        vector<vector<pair<int, int>>> g(n); // 邻接表
        for (auto &t : times) {
            g[t[0] - 1].emplace_back(t[1] - 1, t[2]);
        }

        vector<int> dis(n, INT_MAX);
        dis[k - 1] = 0;
        // pair<int, int> 每个元素类型
        // vector<pair<int, int>> 堆类型
        // greater<> 最小堆；less<> 堆大堆
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        pq.emplace(0, k - 1);
        while (!pq.empty()) {
            auto [dx, x] = pq.top();  // C++的拆包方式
            pq.pop();
            if (dx > dis[x]) { // x 之前出堆过
                continue;
            }
            for (auto &[y, d] : g[x]) {
                int new_dis = dx + d;
                if (new_dis < dis[y]) {
                    dis[y] = new_dis; // 更新 x 的邻居的最短路
                    pq.emplace(new_dis, y);
                }
            }
        }
        int mx = ranges::max(dis);
        return mx < INT_MAX ? mx : -1;
    }
};
