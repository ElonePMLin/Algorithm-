/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// Integer.numberOfLeadingZeros(int)  获取前导 0
class FindElements {
    private final TreeNode root;  // 定义私有且不变对象

    public FindElements(TreeNode root) {
        this.root = root;
    }

    public boolean find(int target) {
        target++;
        TreeNode cur = root;
        for (int i = 30 - Integer.numberOfLeadingZeros(target); i >= 0; i--) {
            int bit = (target >> i) & 1;
            cur = bit == 0 ? cur.left : cur.right;
            if (cur == null) {
                return false;
            }
        }
        return true;
    }
}