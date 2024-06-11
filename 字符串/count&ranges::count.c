class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int cnt = count(s.begin(), s.end(), '1');  // 必须为字符对象 即'1'，不能是"1"；下同。
        return string(cnt - 1, '1') + string(s.length() - cnt, '0') + '1';
    }
};

// 计算字符串含字符数的方法
// count和ranges::count是不一样的吗？
// count(s, '1'); 不能运行，no matching function for call to 'count'
// 可以运行的方法
// ranges::count(s, '1');
// ranges::count(s.begin(), s.end(), '1');
// count(s.begin(), s.end(), '1');
class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int cnt1 = ranges::count(s, '1');
        return string(cnt1 - 1, '1') + string(s.length() - cnt1, '0') + '1';
    }
};

// string object
// string(length, char), 创建长为length的重复char字符串
// s.begin()  起始索引
// s.end()  结束索引
