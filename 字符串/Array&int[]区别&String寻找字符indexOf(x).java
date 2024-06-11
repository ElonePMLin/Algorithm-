class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        // int[] ans = new int[];  int[4]是定义给定范围的，类似C++的array<int, 4>
        List<Integer> ans = new ArrayList<>();
        // .indexOf(x) != -1
        // .add(i)
         for (int i = 0; i < words.length; i++) {
            if (words[i].indexOf(x) != -1) {
                ans.add(i);
            }
         }
         return ans;
    }
}