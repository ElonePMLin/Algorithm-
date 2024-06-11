class Solution {
    public int[] resultArray(int[] nums) {
        List<Integer> l = new ArrayList<>() {{add(nums[0]);}}, r = new ArrayList<>() {{add(nums[1]);}};
        for (int i = 2; i < nums.length; i++) {
            if (l.get(l.size() - 1) > r.get(r.size() - 1)) {
                l.add(nums[i]);
            } else {
                r.add(nums[i]);
            }
        }
        l.addAll(r);
        for (int i = 0; i < nums.length; i++) {
            nums[i] = l.get(i);
        }
        return nums;
    }
}