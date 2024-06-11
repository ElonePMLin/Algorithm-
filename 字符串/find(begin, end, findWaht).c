class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> ans;
        for (int i = 0; i < words.size(); i++) {
            string& word = words[i];
            // find(开始指针， 结束指针， 找的值) 不存在则为结束指针
            if (find(word.begin(), word.end(), x) != word.end()) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};
