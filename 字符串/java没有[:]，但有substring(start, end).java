// String 获取长度 .length()

class Solution {
    public String dynamicPassword(String password, int target) {
        return password.substring(target, password.length()) + password.substring(0, target);
    }
}