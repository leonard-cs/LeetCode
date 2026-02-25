public class TreeNode
{
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }
}


public class Solution
{
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)
    {
        // 1. p, q different side of root => return root
        if ((p.val < root.val && root.val < q.val) || (q.val < root.val && root.val < p.val))
            return root;

        // 2. root equals p or q => return p or q
        if (root.val == p.val)
            return p;
        if (root.val == q.val)
            return q.val;

        if (p.val > root.val)
        {
            root = root.right;
        }
        else
        {
            root = root.left;
        }
        return LowestCommonAncestor(root, p, q);
    }
}