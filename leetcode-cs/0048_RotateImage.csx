public class Solution
{
    public void Rotate(int[][] matrix)
    {
        int l = 0;
        int r = matrix.Length - 1;
        while (l < r)
        {
            for (int i = 0; i < r - l; i++)
            {
                int top = l;
                int bottom = r;
                // save top-left
                int topLeft = matrix[top][l + i];

                // bottom-left -> top-left
                matrix[top][l + i] = matrix[bottom - i][l];

                // bottom-right -> bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i];

                // top-right -> bottom-right
                matrix[bottom][r - i] = matrix[top + i][r];

                // top-left -> bottom-right
                matrix[top + i][r] = topLeft;
            }
            l++;
            r--;
        }
        return;
    }
}