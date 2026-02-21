Console.WriteLine(Solution.CarFleet(10, [4, 1, 0, 7], [2, 2, 1, 1]));

public static class Solution
{
    public static int CarFleet(int target, int[] position, int[] speed)
    {
        var cars = position
            .Select((pos, i) => new { Position = pos, Speed = speed[i] })
            .OrderByDescending(c => c.Position)
            .ToList();

        Stack<float> stack = new Stack<float>();
        foreach (var car in cars)
        {
            float time = (float)(target - car.Position) / car.Speed;
            if (stack.Count == 0 || time > stack.Peek())
            {
                stack.Push(time);
            }
        }
        return stack.Count;
    }
}