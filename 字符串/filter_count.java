class Solution {
    public String maximumOddBinaryNumber(String s) {
        int cnt = 0;
        for (int i = 0; i < s.length(); i++) {
            cnt += s.charAt(i) - '0';  // 字符仅相差1，
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < cnt - 1; i++) {
            sb.append('1');
        }
        for (int i = 0; i < s.length() - cnt; i++) {
            sb.append('0');
        }
        sb.append('1');
        return sb.toString();
    }
}

// string.repeat(count); return the repeat string, or return an empty string(if count eq 0)
// string.chars(); It return an IntStream.
// The stream contains the integer code point values of the characters in the string object.
// 即包含每个字符所对应的char值
// IntStream.forEach(xxx)  默认传入的是每一个字符
// IntStream.filter(xxx).count()  默认传入的是每一个字符，计算符合要求的字符个数
public class Solution {
    public String maximumOddBinaryNumber(String s) {
        int cnt1 = (int) s.chars().filter(c -> c == '1').count();
        return "1".repeat(cnt1 - 1) + "0".repeat(s.length() - cnt1) + "1";
    }
}