class Solution {
    public int scoreOfString(String s) {
        char[] S = s.toCharArray();
        int ans = 0;
        for (int i = 1; i < S.length; i++) {
            ans += Math.abs(S[i - 1] - S[i]);
        }
        return ans;
    }
}