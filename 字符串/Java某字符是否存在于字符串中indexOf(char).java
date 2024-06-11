// VOWEL.indexOf(start)  不存在即为-1
class Solution {
    private static final String VOWEL = "aeiou";

    public int vowelStrings(String[] words, int left, int right) {
        int ans = 0;
        for (int i = left; i <= right; i++) {
            String w = words[i];
            char start = w.charAt(0), end = w.charAt(w.length() - 1);
            if (VOWEL.indexOf(start) != -1 && VOWEL.indexOf(end) != -1) {
                ans++;
            }
        }
        return ans;
    }
}