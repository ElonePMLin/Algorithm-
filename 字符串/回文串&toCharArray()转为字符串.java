class Solution {
    public String makeSmallestPalindrome(String s) {
        char[] c = s.toCharArray();
        for (int i = 0, n = c.length; i < n / 2; i++) {
            char left = c[i];
            char right = c[n - i - 1];
            if (left > right) {
                c[i] = right;
            } else {
                c[n - 1- i] = left;
            }
        }
        return new String(c);
    }
}