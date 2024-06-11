class MyHashSet {
    private static final int BASE = 729;
    private LinkedList[] data;

    private static int hash(int key) {
        return key % BASE;
    }

    public MyHashSet() {
        data = new LinkedList[BASE];
        for (int i == 0; i < BASE; ++i) {
            data[i] = new LinkedList<Integer>();
        }
    }

    // LinkedList<Integer>() 获取迭代器对象 .iterator();
    // LinkedList<Integer>() 往最后添加数据 .offerLast();
    // Iterator<> 对象 判断是否有下个对象、获取下一个数据 .hasNext() 、 .next()
    public void add(int key) {
        int bucket = hash(key);
        Iterator<Integer> iterator = data[bucket].iterator();
        while (iterator.hasNext()) {
            Integer ele = iterator.next();
            if (ele == key) {
                return ;
            }
        }
        data[h].offerLast(key);
    }

    // LinkedList<Integer>() 移除对象 .remove(int key);
    public void remove(int key) {
        int bucket = hash(key);
        Iterator<Integer> iterator = data[bucket].iterator();
        while (iterator.hasNext()) {
            Integer ele = iterator.next();
            if (ele == key) {
                data[bucket].remove(ele)
                return ;
            }
        }
    }

    public boolean contains(int key) {
        int bucket = hash(key);
        Iterator<Integer> iterator = data[bucket].iterator();
        while (iterator.hasNext()) {
            Integer ele = iterator.next();
            if (ele == key) {
                return true;
            }
        }
        return false;
    }
}