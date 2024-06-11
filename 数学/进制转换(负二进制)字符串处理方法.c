class Solution {
public:
    string baseNeg2(int n) {
        if (n == 0 || n == 1) {
            return to_string(n);  // 将整数转换为字符串
        }
        string ans;
        while (n != 0) {
            int v = n & 1;
            ans.push_back('0' + v);  // 若无 '0'，则会导致 乱码 0 + 1 == 1；0 + 0 == 0；
            n = -(n >> 1);
        }
        reverse(ans.begin(), ans.end());  // 传入开始和结束指针，进行反转
        return ans;
    }
};