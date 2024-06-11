class Solution {
public:
    int findMinimumTime(vector<vector<int>>& tasks) {
        ranges::sort(tasks.begin(), tasks.end(), [&](auto a, auto b) { return a[1] < b[1]; });
        vector<array<int, 3>> runned{{-2, -2, 0}};  // array<int, 3> == int runned[3] = {x, y, z}; 可以拆包
        for (auto& t : tasks) {
            int start = t[0], end = t[1], duration = t[2];
            // *取值
            // ranges::lower_bound(target, value, comp, proj)
            // auto [_, ed, dur] = *--ranges::lower_bound(runned, start, {}, [](auto& x) { return x[0]; });

            // std::lower_bound(first, last, value, comp, proj)
            // int k = lower_bound(st.begin(), st.end(), start, [&](const vector<int> &a, const int b) -> bool {
            //    return a[0] < b;
            // }) - st.begin();
            auto [_, ed, dur] = *--ranges::lower_bound(runned, start, {}, [](auto& x) { return x[0]; });
            duration -= runned.back()[2] - dur;
            if (start <= ed) {
                duration -= ed - start + 1;
            }
            if (duration <= 0) continue;

            while (end - runned.back()[1] <= duration) {
                auto [st, ed, _] = runned.back();  // 取最后
                runned.pop_back();  // 使最后元素退出
                duration += ed - st + 1;
            }
            runned.push_back({end - duration + 1, end,runned.back()[2] + duration});
        }
        return runned.back()[2];
    }
};