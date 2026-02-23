Console.WriteLine(Solution.HasAllCodes("00110", 2));

public static class Solution
{
    public static bool HasAllCodes(string s, int k)
    {
        HashSet<string> set = new HashSet<string>();
        for (int i = 0; i <= s.Length - k; i++)
        {
            set.Add(s.Substring(i, k));

            if (set.Count == Math.Pow(2, k))
                return true;
        }
        Console.WriteLine(string.Join(", ", set));
        return false;
    }
}