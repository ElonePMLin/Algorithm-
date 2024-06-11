// 取最大最小方法
//      auto [m, M] = ranges::minmax(salary);  // 获取最小最大值
//      reduce(salary.begin(), salary.end());  // 总和
class Solution {
public:
    double average(vector<int>& salary) {
        int s = reduce(salary.begin(), salary.end());
        auto [m, M] = ranges::minmax(salary);
        return (double) (s - m - M) / (salary.size() - 2);
    }
};


// 排序方法
//      ranges::sort(salary, [&](int i, int j) { return i < j });  // 排序
//      std:accumulate(salary.begin() + 1, salary.end() - 1, 0);  // 总和
class Solution {
public:
    double average(vector<int>& salary) {
        ranges::sort(salary, [&](int i, int j) {
            return i < j;
        });
        double sum = std::accumulate(salary.begin() + 1, salary.end() - 1, 0);
        return sum / (salary.size() - 2);
    }
};
