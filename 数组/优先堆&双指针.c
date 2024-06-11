class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int candidates) {
        int n = costs.size();
        if (n - 2 * candidates < k) {
            ranges::nth_element(costs, costs.begin() + k);  // 排序 ranges::nth_element(data, end)
            // 0LL 从0开始，为long long类型，相加，accumulate(start, end, type)
            return accumulate(costs.begin(), costs.begin() + k, 0LL);
        }

        priority_queue<int, vector<int>, greater<>> pre, suf;  // 优先堆
        for (int i = 0; i < candidates; i++) {
            pre.push(costs[i]);
            suf.push(costs[n - i - 1]);
        }

        // 双指针
        long long ans = 0;
        int i = candidates, j = n - candidates - 1;
        while (k--) {
            if (pre.top() <= suf.top()) {
                ans += pre.top();
                pre.pop();
                pre.push(costs[i++]);
            } else {
                ans += suf.top();
                suf.pop();
                suf.push(costs[j--]);
            }
        }
        return ans;
    }
};