class Solution {
    public int garbageCollection(String[] garbage, int[] travel) {
        int ans = 0, dis = 0;
        int[] mp = new int[4];
        for (int i = 0; i < garbage.length; i++) {
            String g = garbage[i];
            int n = g.length();
            ans += n;
            dis += i != 0 ? travel[i - 1] : 0;
            for (int j = 0; j < n; j++) {
                char c = g.charAt(j);
                // M & 3 = 1
                // P & 3 = 0
                // G & 3 = 3
                // 因此需要 int[] mp = new int[4];
                ans += dis - mp[c & 3];
                mp[c & 3] = dis;
            }
        }
        return ans;
    }
}