// 该方法只是学习双端列表，实际仅用StringBuilder即可

class Solution {
    public String finalString(String s) {
        Deque<Character> q = new ArrayDeque<>();
        boolean flag = true;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'i') {
                flag = !flag;
                continue;
            }
            if (flag) {
                q.addLast(c);
            } else {
                q.addFirst(c);
            }
        }

        StringBuilder ans = new StringBuilder();
        for (char c : q) {
            ans.append(c);
        }
        if (!flag) {
            ans.reverse();
        }
        return ans.toString();
    }
}