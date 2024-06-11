// 利用分桶思想(链地址法) 设计哈希集合
// list<>  链表数据结构
class MyHashSet {
private:
    vector<list<int>> data;
    static const int base = 729;
    static int hash(int key) {
        return key % base;
    }
public:
    // 构造方法
    MyHashSet(): data(base) {}

    // list<int> 起始数据、结束数据、往最后添加数据方法 .begin()  .end()  .push_back(int key)
    // 这里 it 是 List<int>
    void add(int key) {
        int bucket = hash(key);
        for (auto it = data[bucket].begin(); it != data[bucket].end(); it++) {
            if ((*it) == key) {
                return ;
            }
        }
        data[bucket].push_back(key);
    }

    // list<int> 移除数据方法  .erase(int key)
    void remove(int key) {
        int bucket = hash(key);
        for (auto it = data[bucket].begin(); it != data[bucket].end(); it++) {
            if ((*it) == key) {
                data[bucket].erase(it);
                return ;
            }
        }
    }

    bool contains(int key) {
        int bucket = hash(key);
        for (auto it = data[bucket].begin(); it != data[bucket].end(); it++) {
            if ((*it) == key) {
                return true;
            }
        }
        return false;
    }
}

// leetcode运行时间快的代码例子
class MyHashSet {
    int hash[1000001];
public:
    MyHashSet() {
        memset(hash,0,sizeof(hash));
    }

    void add(int key) {
        hash[key]=1;
    }

    void remove(int key) {
        hash[key]=0;
    }

    bool contains(int key) {
        return hash[key];
    }
};

