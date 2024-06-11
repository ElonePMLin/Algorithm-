// accumulate() 方法，需要给定初始值
class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        int end = k > 0 ? k + 1 : n;
        k = abs(k);
        vector<int> ans(n);
        int s = accumulate(code.begin() + end - k, code.begin() + end, 0);
        for (int i = 0; i < n; i++) {
            ans[i] = s;
            s += code[end % n] - code[(end - k) % n];
            end += 1;
        }
        return ans;
    }
};


// reduce() 方法，不需要给定初始值
class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        int end = k > 0 ? k + 1 : n;
        k = abs(k);
        vector<int> ans(n);
        int s = reduce(code.begin() + end - k, code.begin() + end);
        for (int i = 0; i < n; i++) {
            ans[i] = s;
            s += code[end % n] - code[(end - k) % n];
            end += 1;
        }
        return ans;
    }
};
