class Solution {
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        int ans = 0;
        bool seen[26][26]{};
        for (auto& w : words) {
            int x = w[0] - 'a';
            int y = w[1] - 'a';
            if (seen[y][x]) {
                ans++;
            } else {
                seen[x][y] = true;
            }
        }
        return ans;
    }
};


// unordered_set<string> seen;
//      .count(val);
//      .insert(val);
class Solution {
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        int ans = 0;
        unordered_set<string> seen;  // 红黑树集合
        for (auto& w : words) {
            string tmp = w;
            reverse(w.begin(), w.end());  // 反转字符串
            if (seen.count(w)) {  // 是否存在
                ans++;
            } else {
                seen.insert(tmp);  // 插入
            }
        }
        return ans;
    }
};
