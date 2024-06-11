class Solution {
public:
    vector<string> splitWordsBySeparator(vector<string>& words, char separator) {
        vector<string> res;
        for (string &word : words) {
            stringstream ss(word);  // 字符串流
            string sub;
            // getline(input, str, delim)  // input从流中获取数据；str放置数据的字符；delim分割符
            // 好像效率低
            while (getline(ss, sub, separator)) {
                if (!sub.empty()) {
                    res.push_back(sub);
                }
            }
        }
        return res;
    }
};


class Solution {
public:
    vector<string> splitWordsBySeparator(vector<string>& words, char separator) {
        vector<string> ans;
        for (string w : words) {
            string word;
            for (char c : w) {
                if (c == separator && word != "") {
                    ans.push_back(word);
                    word = "";
                } else if (c != separator) {
                    word.push_back(c);
                }
            }
            if (word != "") {
                ans.push_back(word);
            }
        }
        return ans;
    }
};