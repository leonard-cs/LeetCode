Console.WriteLine(Solution.LeastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2));

public static class Solution
{
    public static int LeastInterval(char[] tasks, int n)
    {
        int[] counts = new int[26];
        foreach (var ch in tasks)
        {
            int index = (int)ch - (int)'A';
            counts[index]++;
        }

        var maxHeap = new PriorityQueue<int, int>();
        foreach (var count in counts)
        {
            if (count > 0)
                maxHeap.Enqueue(count, -count); // max heap
        }

        var cooldown = new Queue<(int count, int readyTime)>();
        int clock = 0;
        while (maxHeap.Count > 0 || cooldown.Count > 0)
        {
            if (cooldown.Count > 0 && cooldown.Peek().readyTime == clock)
            {
                var task = cooldown.Dequeue();
                maxHeap.Enqueue(task.count, -task.count);
            }
            if (maxHeap.Count > 0)
            {
                int remaining = maxHeap.Dequeue() - 1;

                if (remaining > 0)
                    cooldown.Enqueue((remaining, clock + n + 1));
            }
            clock++;
        }

        return clock;
    }
}