public class Solution
{
    public int MaximumDifference(int[] nums)
    {
        int result = -1;

        int[] prefixMin = new int[nums.Length];
        prefixMin[0] = nums[0];
        for (int i = 1; i < nums.Length; i++)
        {
            prefixMin[i] = Math.Min(prefixMin[i - 1], nums[i]);
        }
        
        for (int i = 1; i < nums.Length; i++)
        {
            int diff = nums[i] - prefixMin[i - 1];
            if (diff > 0)
                result = Math.Max(result, nums[i] - prefixMin[i - 1]);
        }
        return result;
    }
}