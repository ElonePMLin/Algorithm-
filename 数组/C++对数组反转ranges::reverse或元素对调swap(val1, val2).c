class Solution {
public:
    void reverseString(vector<char>& s) {
        ranges::reverse(s);
        return ;
    }
};


class Solution {
public:
    void reverseString(vector<char>& s) {
        int l = 0, r = s.size() - 1;
        for (;l < r; l++, r--) {
            swap(s[l], s[r]);
        }
        return ;
    }
};
