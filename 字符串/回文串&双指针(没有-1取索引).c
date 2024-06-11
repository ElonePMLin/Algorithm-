class Solution {
public:
    string makeSmallestPalindrome(string s) {
        int n = s.length();
        for (int i = 0; i < n / 2; i++) {
            char left = s[i], right = s[n -1 -i];
            if (left > right) {
                s[i] = right;
            } else {
                s[n -1 - i] = left;
            }
        }
        return s;
    }
};
