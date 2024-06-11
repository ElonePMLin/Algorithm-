class OrderedStream {
// 定义变量
private:
    int ptr;
    vector<string> arr;

public:
    OrderedStream(int n) {
        // 给变量赋值
        ptr = 1;
        arr.resize(n);  // 或者 arr = vector<string>(n, " ");
    }

    vector<string> insert(int idKey, string value) {
        arr[idKey - 1] = value;
        vector<string> ans;
        if (idKey == ptr) {
            for (int i = idKey - 1; i < arr.size(); i++) {
                if (arr[i].empty()) {  // arr[i].empty()  判断该指针值是否为空
                    ptr = i + 1;
                    break;
                }
                ans.push_back(arr[i]);
            }
        }
        return ans;
    }
};