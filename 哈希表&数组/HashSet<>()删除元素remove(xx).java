class Solution {
    public int[] numberOfPairs(int[] nums) {
        int pair = 0, n = nums.length;
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                pair++;
                seen.remove(num);
            } else {
                seen.add(num);
            }
        }
        return new int[]{pair, n - pair * 2};
    }
}