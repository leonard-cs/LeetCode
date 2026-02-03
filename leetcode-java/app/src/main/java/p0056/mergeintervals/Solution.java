package p0056.mergeintervals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public static int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (inter1, inter2) -> Integer.compare(inter1[0], inter2[0]));
        System.out.println(Arrays.deepToString(intervals));
        List<int[]> result = new ArrayList<>();
        result.add(intervals[0]);
        for (int i = 1; i < intervals.length; i++) {
            int[] a = result.get(result.size() - 1);
            int[] b = intervals[i];
            if (b[0] <= a[1]) {
                int end = Math.max(a[1], b[1]);
                int[] inter = {a[0], end};
                result.set(result.size() - 1, inter);
            } else {
                result.add(b);
            }
        }
        return result.toArray(new int[result.size()][]);
    }

    public static void main(String[] args) {
        int [][] intervals = {{1,3},{2,6},{8,10},{15,18}};
        int [][] result = merge(intervals);
        System.out.println(Arrays.deepToString(result));
    }
}
