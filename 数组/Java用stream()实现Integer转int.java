class Solution {
    public int[] decompressRLElist(int[] nums) {
        int n = nums.length;
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < n; i += 2) {
            for (int j = 0; j < nums[i]; j++) {
                ans.add(nums[i + 1]);
            }
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();  // 流
    }
}