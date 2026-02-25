public class TreeNode
{
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution
{
    public int SumRootToLeaf(TreeNode root)
    {
        return SumLeaf(root, 0);
    }

    private int SumLeaf(TreeNode node, int current)
    {
        if (node == null)
            return 0;

        current = (current << 1) | node.val;

        if (node.left == null && node.right == null)
            return current;

        return SumLeaf(node.left, current) + 
               SumLeaf(node.right, current);
    }
}
// [1], 2 => 5
// [1], 1 => 3
// [0, 1], 1 => 5
// [1, 0, 1, 1], 0 => 5 + 3