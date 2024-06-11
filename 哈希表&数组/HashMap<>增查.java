// mp = new HashMap<>()
//      .containsKey(k)  查
//      .get(k)  查
//      .put(k, v)  增

class Solution {
    public String decodeMessage(String key, String message) {
        Map<Character, Character> mp = new HashMap<>() {{
            put(' ', ' ');
        }};
        char idx = 'a';
        for (int i = 0; i < key.length(); i++) {
            char k = key.charAt(i);
            if (!mp.containsKey(k)) {
                mp.put(k, idx);
                idx++;
            }
        }

        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < message.length(); i++) {
            ans.append(mp.get(message.charAt(i)));
        }
        return ans.toString();
    }
}