class Solution {
    public int[] sortByBits(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int i : arr) {
            list.add(i);
        }
        Collections.sort(list, new Comparator<Integer>() {
            public int compare(Integer i, Integer j) {
                int x = Integer.bitCount(i), y = Integer.bitCount(j);
                if (x == y) {
                    return i - j;
                }
                return x - y;
            }
        });

        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}