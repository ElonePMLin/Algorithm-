class Solution {
public:
    int splitNum(int num) {
        string s = to_string(num);
        sort(s.begin(), s.end());
        int pocket[2];
        for (int i = 0; i < s.size(); i++) {
            pocket[i % 2] = pocket[i % 2] * 10 + s[i] - '0';
        }
        return pocket[0] + pocket[1];
    }
};