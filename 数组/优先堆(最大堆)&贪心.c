class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        int n = quality.size(), q_sum = 0;
        vector<int> idx(n);
        std::iota(idx.begin(), idx.end(), 0);  // 递增0，idx是 wage / quality 的顺序。对于 int[n] 不适用
        ranges::sort(idx, [&](int i, int j) {
            return wage[i] * quality[j] < wage[j] * quality[i];  // 用 / 会错，原因？
        });
        priority_queue<int, vector<int>, less<>> pq;  // 等同 priority_queue<int>，C++默认为最大堆
        for (int i = 0; i < k; i++) {
            pq.push(quality[idx[i]]);
            q_sum += quality[idx[i]];
        }

        double res = q_sum * ((double) wage[idx[k - 1]] / quality[idx[k - 1]]);  // 转为 double

        for (int i = k; i < n; i++) {
            int q = quality[idx[i]];
            if (pq.top() > q) {
                q_sum -= pq.top() - q;
                pq.pop();
                pq.push(q);
                res = min(res, q_sum * ((double) wage[idx[i]] / q));
            }
        }
        return res;
    }
};