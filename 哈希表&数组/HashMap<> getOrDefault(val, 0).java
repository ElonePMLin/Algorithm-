class Solution {
    public int numIdenticalPairs(int[] nums) {
        int count=0;
        Map<Integer,Integer> map=new HashMap<>();

        for (int num : nums) {
            int value = map.getOrDefault(num,0);  // 不存在则设置为 0
            count += value;
            map.put(num,value+1);
        }
        return count;
    }
}