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
class Solution {
    private int count;

    public int averageOfSubtree(TreeNode root) {
        count = 0;
        helper(root);
        return count;
    }

    private void helper(TreeNode root){
        if(root==null){
            return;
        }

        // calculating the sum of all nodes from current subtree
        int sum = getSum(root.left) + getSum(root.right) + root.val;
        // counting number of nodes in the current subtree
        int n = numOfNodes(root.left) + numOfNodes(root.right) + 1;

        if(n!=0 && root.val==sum/n){
            count++;
        }

        helper(root.left);
        helper(root.right);
    }

    private int getSum(TreeNode root){
        if(root==null){
            return 0;
        }

        return getSum(root.left) + getSum(root.right) + root.val;
    }

    private int numOfNodes(TreeNode root){
        if(root==null){
            return 0;
        }

        return numOfNodes(root.left) + numOfNodes(root.right) + 1;
    }
}