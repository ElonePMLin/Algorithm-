class Solution {
public:
    vector<string> cellsInRange(string s) {
        vector<string> ans;
        char start = s[0], end = s[3];
        for (;start <= end; start++) {
            for (char i = s[1]; i <= s[4]; i++) {
                string c(1, start);
                c.push_back(i);
                ans.push_back(c);
            }
        }
        return ans;
    }
};