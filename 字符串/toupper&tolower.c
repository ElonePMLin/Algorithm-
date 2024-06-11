class Solution {
public:
    string capitalizeTitle(string title) {
        int n = title.size();
        int l = 0, r = 0;   // 单词左右边界（左闭右开），必须定义为 0，否则默认不为 0
        while (r < n) {
            while (r < n && title[r] != ' ') {
                ++r;
            }
            // 对于每个单词按要求处理
            if (r - l > 2) {
                title[l++] = toupper(title[l]);
            }
            while (l < r) {
                title[l++] = tolower(title[l]);
            }
            l = ++r;
        }
        return title;
    }
};


// istringstream iss(title);  解析字符串，将要解析的字符串传递给它
// string s; iss >> s; 将尝试从title中提取一个字符串(以空格为界) 输入操作符 >> 提取数据
// 如果提取成功 iss 和 iss >> s; 返回 true;
// s 为提取到的数据
// tolower(char)、toupper(char)
// length() 和 size()有什么区别？
// 没有区别，length是因为沿用C语言的习惯而保留下来的，string类最初只有length，
// 引入STL之后，为了兼容又加入了size，它是作为STL容器的属性存在的，便于符合STL的接口规则，以便用于STL的算法。
class Solution {
public:
    string capitalizeTitle(string title) {
        istringstream iss(title);
        string ans, s;
        while (iss >> s) {
            if (!ans.empty()) {
                ans += ' ';
            }
            if (s.length() > 2) {
                ans += toupper(s[0]); // 首字母大写
                s = s.substr(1);  // 截取索引1后的字符串
            }
            for (char c : s) {
                ans += tolower(c);
            }
        }
        return ans;
    }
};
