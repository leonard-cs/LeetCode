package p0119.pascalsTriangleII;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<>();
        row.add(1);
        for (int r = 1; r <= rowIndex; r++) {
            List<Integer> newRow = new ArrayList<>();
            newRow.add(1);
            for (int i = 1; i < r; i++) {
                newRow.add(row.get(i-1) + row.get(i));
            }
            newRow.add(1);
            row = newRow;
        }
        return row;
    }
}
