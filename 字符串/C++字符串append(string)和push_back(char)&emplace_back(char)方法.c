class Solution {
public:
    string defangIPaddr(string address) {
        string ans;
        for (char s : address) {
            if (s == '.') {
                ans += "[.]";  // ans.append("[.]")
            } else {
                ans += s;  // ans.push_back(s) & ans.emplace_back(s)
            }
        }
        return ans;
    }
};