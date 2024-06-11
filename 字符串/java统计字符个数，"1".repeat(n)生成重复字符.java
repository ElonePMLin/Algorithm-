class Solution {
    public String maximumOddBinaryNumber(String s) {
        int cnt = (int) s.chars().filter(c -> c == '1').count();
        return "1".repeat(cnt - 1) + "0".repeat(s.length() - cnt) + "1";
    }
}