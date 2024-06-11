class Solution {
    public int countPairs(List<Integer> nums, int target) {
        // List是Collections，不是 Arrays -> int[]
        Collections.sort(nums, (i, j) -> (i - j));
        int n = nums.size();  // List 用 .size()
        int ans = 0;
        for (int l = 0, r = n - 1; l < r; ) {
        // if (nums[l] + nums[r] < target) {
        // List 用 .get(index)，不是 [] 取索引的方式
            if (nums.get(l) + nums.get(r) < target) {
                ans += r - l;
                l++;
            } else {
                r--;
            }
        }
        return ans;
    }
}

// 另一种情况就是转换List 为 Arrays
Integer[] arr = nums.toArray(new Integer[nums.size()]);
