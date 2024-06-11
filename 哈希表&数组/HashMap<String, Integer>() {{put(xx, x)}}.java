class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int idx = new HashMap<String, Integer>() {{
            put("type", 0);
            put("color", 1);
            put("name", 2);
        }}.get(ruleKey);  // HashMap获取值
        int ans = 0;
        for (List<String> item : items) {
            if (item.get(idx).equals(ruleValue)) {  // String对比值
                ans++;
            }
        }
        return ans;
    }
}
