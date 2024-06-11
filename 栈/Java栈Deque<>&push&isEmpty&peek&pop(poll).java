class Solution {
    public int minLength(String s) {
        Deque<Character> st = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (!st.isEmpty() && (c == 'B' && st.peek() == 'A' || c == 'D' && st.peek() == 'C')) {
                st.poll();  // st.pop();
            } else {
                st.push(c);
            }
        }
        return st.size();
    }
}