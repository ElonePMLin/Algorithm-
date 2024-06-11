// unordered_set<int> valSet;  a set of unique objects of type Key
// .insert(int)、.count(int)
class FindElements {
private:  // 定义私有属性
    unordered_set<int> valSet;  // 无序集合

    void dfs(TreeNode *node, int val) {
        if (node == nullptr) {  // 指针为空
            return;
        }
        node->val = val;  // 取指针指向的对象 ->
        valSet.insert(val);
        dfs(node->left, val * 2 + 1);
        dfs(node->right, val * 2 + 2);
    }

public:
    FindElements(TreeNode* root) {
        dfs(root, 0);
    }

    bool find(int target) {
        return valSet.count(target) > 0;
    }
};


class FindElements {
    TreeNode *root;  // 定义公共属性
public:
    FindElements(TreeNode *root) : root(root) {}  // 定义公共或私有对象root的属性

    bool find(int target) {
        target++;
        auto cur = root; // 从根节点出发，auto使cur的对象为root对象
        for (int i = 30 - __builtin_clz(target); i >= 0; i--) { // 从次高位开始枚举，__builtin_clz() 前导0的个数
            int bit = target >> i & 1; // target 第 i 位的比特值
            cur = bit ? cur->right : cur->left;
            if (cur == nullptr) { // 走到空节点，说明 target 不在二叉树中
                return false;
            }
        }
        return true; // 没有走到空节点，说明 target 在二叉树中
    }
};