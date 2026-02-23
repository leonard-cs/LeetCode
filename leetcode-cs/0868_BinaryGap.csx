Console.WriteLine(Solution.BinaryGap(7));

public static class Solution
{
    public static int BinaryGap(int n)
    {
        int prevOneIndex = -1;
        int maxGap = 0;
        int currIndex = 0;
        while (n > 0)
        {
            if ((n & 1) == 1)
            {
                if (prevOneIndex != -1)
                {
                    maxGap = Math.Max(maxGap, currIndex - prevOneIndex);
                }
                prevOneIndex = currIndex;
            }
            currIndex++;
            n >>= 1;
        }
        return maxGap;
    }
}