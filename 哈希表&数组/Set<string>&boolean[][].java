class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
        int ans = 0;
        boolean[][] seen = new boolean[26][26];
        for (String w : words) {
            int x = w.charAt(0) - 'a';  // 字符串操作，string.charAt(index)
            int y = w.charAt(1) - 'a';
            if (seen[y][x]) {
                ans++;
            } else {
                seen[x][y] = true;
            }
        }
        return ans;
    }
}


// Set<String> seen = new HashSet<>();
//      .contains(val);
//      .add(val);
class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
        int ans = 0;
        Set<String> seen = new HashSet<>();
        for (String w : words) {
            if (seen.contains(new StringBuilder(w).reverse().toString())) {
                ans++;
            } else {
                seen.add(w);
            }
        }
        return ans;
    }
}
