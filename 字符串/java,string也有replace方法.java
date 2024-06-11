class Solution {
    public String interpret(String command) {
        char[] arr = command.toCharArray();
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            if (command.charAt(i) == 'G') {
                ans.append("G");
            } else if (command.charAt(i) == '(') {
                ans.append(command.charAt(i + 1) == ')' ? "o" : "al");
            }
        }
        return ans.toString();
    }
}


class Solution {
    public String interpret(String command) {
        return command.replace("()","o").replace("(al)","al");
    }
}

