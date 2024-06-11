// 具体分析在.py文件中，C++不建议对原数组进行修改操作，若容器中的数组相加后的超过int范围会报错！！！
class Solution {
public:
    long long maxArrayValue(vector<int> &nums) {
        long long sum = nums.back();
        for (int i = nums.size() - 2; i >= 0; i--) {
            sum = nums[i] <= sum ? sum + nums[i] : nums[i];
        }
        return sum;
    }
};

// vector, .back() 取最后一个元素的值; .size() 容器(数组)大小
// C++ 定义数组 用 容器 vector<int> nums
