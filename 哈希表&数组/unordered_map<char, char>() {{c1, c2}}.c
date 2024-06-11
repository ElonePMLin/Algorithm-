// unordered_map<> mp;
//      .contains(val); 和 .count(val); 一样
class Solution {
public:
    string decodeMessage(string key, string message) {
        unordered_map<char, char> mp = {{' ', ' '}};
        int idx = 0;
        for (int i = 0; i < key.length(); i++) {
            char k = key[i];
            if (!mp.contains(k)) {
                mp[k] = (char) (97 + idx);
                idx += 1;
            }
        }
        string ans;
        for (int i = 0; i < message.length(); i++) {
            ans.push_back(mp[message[i]]);
        }
        return ans;
    }
};