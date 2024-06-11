class Solution {
    public String replaceDigits(String s) {

        char[] result = new char[s.length()];

        for(int i = 0; i < result.length; i++) {
            if (i % 2 == 0){
                result[i] = s.charAt(i);
            }else {
                char num = s.charAt(i - 1);
                int c = s.charAt(i) - '0';
                int k = num + c;
                result[i] = (char) k;
            }
        }

        return new String(result);  // 数组给String对象即可
    }
}