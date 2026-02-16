package p0118.pascalsTriangle;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> pascal = new ArrayList<>();
        pascal.add(Arrays.asList(1));  // r == 0
        for (int r = 2; r < numRows; r++) {
            List<Integer> prevRow = pascal.get(r - 1);
            List<Integer> row = new ArrayList<>();

            row.add(1);
            for (int i = 1; i < r; i++) {
                row.add(prevRow.get(i - 1) + prevRow.get(i));
            }
            row.add(1);
            pascal.add(row);
        }
        return pascal;
    }
}
