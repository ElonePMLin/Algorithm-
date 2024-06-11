class MyHashMap {
private:
    vector<list<pair<int, int>>> data;
    static const int size = 729;
    static int hash(int key) {
        return key % size;
    }

public:
    MyHashMap(): data(size) {}

    // list<pair<int, int>>  往最后添加数据  .push_back(make_pair(key, value))
    // pair<int, int> 获取数据对的第一个元素、第二个元素 .first  .second
    // 创建一个数据对  make_pair(one, two)
    void put(int key, int value) {
        int bucket = hash(key);
        for (auto it = data[bucket].begin(); it != data[bucket].end(); it++) {
            if ((*it).first == key) {
                (*it).second = value;
                return ;
            }
        }
        data[bucket].push_back(make_pair(key, value));
    }


    int get(int key) {
        int bucket = hash(key);
        for (auto it = data[bucket].begin(); it != data[bucket].end(); it++) {
            if ((*it).first == key) {
                return (*it).second;
            }
        }
        return -1;
    }

    // list<pair<int, int>>  移除数据  .erase(pair<int, int>)
    void remove(int key) {
        int bucket = hash(key);
        for (auto it = data[bucket].begin(); it != data[bucket].end(); it++) {
            if ((*it).first == key) {
                data[bucket].erase(it);
                return ;
            }
        }
    }
};