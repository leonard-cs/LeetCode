package p1382.balanceBST;

import dataStructures.TreeNode;

import java.util.*;

class Solution {
    public TreeNode balanceBST(TreeNode root) {
        List<Integer> inOrderList = inorderTraversal(root);

        int[] nums = inOrderList.stream()
                .mapToInt(Integer::intValue)
                .toArray();

        return build(nums, 0, nums.length - 1);
    }

    private List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;

        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }

            curr = stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }

        return res;
    }

    private TreeNode build(int[] nums, int left, int right) {
        if (left > right) return null;

        int mid = left + (right - left) / 2;

        TreeNode root = new TreeNode(nums[mid]);
        root.left = build(nums, left, mid - 1);
        root.right = build(nums, mid + 1, right);

        return root;
    }
}
