Console.WriteLine(Solution.CountPrimeSetBits(10, 15));

public static class Solution
{
    public static int CountPrimeSetBits(int left, int right)
    {
        int count = 0;
        for (int num = left; num <= right; num++)
        {
            if (HavePrimeSetBits(num))
                count++;
        }
        return count;
    }

    private static bool HavePrimeSetBits(int num)
    {
        int count = 0;
        while (num > 0)
        {
            count += num & 1;
            num >>= 1;
        }

        return IsSmallPrime(count);
    }

    private static bool IsSmallPrime(int num)
    {
        int[] primes = [2, 3, 5, 7, 11, 13, 17, 19];
        return primes.Contains(num);
    }
}
