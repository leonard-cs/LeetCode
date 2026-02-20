int[] nums = [4, 7, 9, 3, 9];
int[] divisors = [5, 2, 3];
Console.WriteLine(Solution.MaxDivScore(nums, divisors));

public static class Solution
{
    public static int MaxDivScore(int[] nums, int[] divisors)
    {
        int maxScore = 0;
        int result = divisors[0];
        foreach (var div in divisors)
        {
            int score = 0;
            foreach (var num in nums)
            {
                if (num % div == 0)
                {
                    score = score + 1;
                }
            }

            if (score > maxScore || (div < result && score == maxScore))
            {
                maxScore = score;
                result = div;
            }
        }
        return result;
    }
}
