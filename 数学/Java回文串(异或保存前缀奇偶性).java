class Solution {
    private static final int DIGITAL = 10;

    public int longestAwesome(String s) {
        int n = s.length();
        int[] pos = new int[1 << DIGITAL];
        Arrays.setAll(pos, i -> n);
        pos[0] = -1;

        int prev = 0, ans = 0;
        for (int i = 0; i < n; i++) {
            prev ^= 1 << (s.charAt(i) - '0');

            ans = Math.max(ans, i - pos[prev]);
            for (int j = 0; j < DIGITAL; j++) {
                ans = Math.max(ans, i - pos[prev ^ (1 << j)]);
            }

            if (pos[prev] == n) {
                pos[prev] = i;
            }
        }
        return ans;
    }
}