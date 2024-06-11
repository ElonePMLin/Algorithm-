class Solution {
    public String capitalizeTitle(String title) {
        StringBuilder sb = new StringBuilder(title);
        int n = title.length();
        int l = 0, r = 0;   // 单词左右边界（左闭右开），必须初始化数值
        while (r < n) {
            while (r < n && sb.charAt(r) != ' ') {
                ++r;
            }
            // 对于每个单词按要求处理
            if (r - l > 2) {
                sb.setCharAt(l, Character.toUpperCase(sb.charAt(l)));
                ++l;
            }
            while (l < r) {
                sb.setCharAt(l, Character.toLowerCase(sb.charAt(l)));
                ++l;
            }
            l = r + 1;
            ++r;
        }
        return sb.toString();
    }
}

// 新键类对象，切记加new
// string object, .substring(start, end) .substring(start) .toUpperCase() .toLowerCase() .length() .split(String)
// StringBuilder object, .append(Char), .append(String), isEmpty() .toString()
//                        .setCharAt(idx, char) .charAt(idx)
// Character.toUpperCase(char)  Character.toLowerCase(char)
// 字符串和字符对象都有toUpperCase toLowerCase 对象，用法不同
public class Solution {
    public String capitalizeTitle(String title) {
        StringBuilder ans = new StringBuilder();
        for (String s : title.split(" ")) {
            if (!ans.isEmpty()) {
                ans.append(' ');
            }
            if (s.length() > 2) {
                ans.append(s.substring(0, 1).toUpperCase()); // 首字母大写
                s = s.substring(1);
            }
            ans.append(s.toLowerCase());
        }
        return ans.toString();
    }
}
