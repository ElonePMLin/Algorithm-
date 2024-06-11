class Solution {
    public int splitNum(int num) {
        char[] s = Integer.toString(num).toCharArray();
        Arrays.sort(s);
        int[] pocket = new int[2];
        for (int i = 0; i < s.length; i++) {
            pocket[i % 2] = pocket[i % 2] * 10 + s[i] - '0';
        }
        return pocket[0] + pocket[1];
    }
}