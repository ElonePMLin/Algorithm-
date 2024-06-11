class Solution {
    public String baseNeg2(int n) {
        if (n == 0 || n == 1) {
            return String.valueOf(n);  // 整数转换为字符串
        }
        StringBuilder ans = new StringBuilder();
        while (n != 0) {
            int v = n & 1;
            ans.append(v);
            n = -(n >> 1);
        }
        return ans.reverse().toString();
    }
}