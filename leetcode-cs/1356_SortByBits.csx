public class Solution
{
    public int[] SortByBits(int[] arr)
    {
        var dict = new SortedDictionary<int, List<int>>();
        foreach (var num in arr)
        {
            int count = BitOperations.PopCount((uint)num);

            if (!dict.ContainsKey(count))
                dict[count] = new List<int>();

            dict[count].Add(num);
        }

        var result = new List<int>();
        foreach (var pair in dict)
        {
            pair.Value.Sort();
            result.AddRange(pair.Value);
        }
        return result.ToArray();
    }
}