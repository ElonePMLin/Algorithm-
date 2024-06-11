class Solution {
    public int[] decrypt(int[] code, int k) {
        int n = code.length;
        int[] ans = new int[n];
        int end = k > 0 ? k + 1 : n;
        k = Math.abs(k);
        int s = 0;
        for (int i = end - k; i < end; i++) {
            s += code[i];
        }

        for (int i = 0; i < n; i++) {
            ans[i] = s;
            s += code[end % n] - code[(end - k) % n];
            end++;
        }
        return ans;
    }
}