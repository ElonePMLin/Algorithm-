// 该方法只是学习双端列表，实际仅用string ans;即可

class Solution {
public:
    string finalString(string s) {
        deque<char> q;
        bool flag = true;

        for (char c : s) {
            if (c == 'i') {
                flag = !flag;
                continue;
            }
            flag ? q.push_back(c): q.push_front(c);
        }
        // rbegin(); rend(); 从右边开始
        return flag ? string(q.begin(), q.end()): string(q.rbegin(), q.rend());
    }
};