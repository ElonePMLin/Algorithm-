// array 定义后空间就不能改变，且效率比vector快
// pair < array < vector
class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int n = startTime.size();
        vector<array<int, 3>> jobs(n);

        for (int i = 0; i < n; i++) {
            jobs[i] = {endTime[i], startTime[i], profit[i]};
        }
        ranges::sort(jobs, [&](auto i, auto j) {
            return i[0] < j[0];
        });

        vector<int> f(n + 1);
        for (int i = 0; i < n; i++) {
            int j = lower_bound(jobs.begin(), jobs.begin() + i, array<int, 3>{jobs[i][1], INT_MAX}) - jobs.begin();
            f[i + 1] = max(f[i], f[j] + jobs[i][2]);
        }
        return f[n];
    }
};