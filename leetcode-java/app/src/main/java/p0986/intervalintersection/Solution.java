package p0986.intervalintersection;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        int i = 0;
        int j = 0;
        List<int[]> intersection = new ArrayList<>();
        while (i < firstList.length && j < secondList.length) {
            int[] a = firstList[i];
            int[] b = secondList[j];
            // check overlap: if start1 <= end2 AND start2 <= end1
             if (a[0] <= b[1] && b[0] <= a[1]) {
                 intersection.add(new int[]{Math.max(a[0], b[0]), Math.min(a[1], b[1])});
             }

             if (a[1] < b[1]) {
                 i++;
             } else if (b[1] < a[1]) {
                 j++;
             } else {
                 i++;
                 j++;
             }
        }
        return intersection.toArray(new int[intersection.size()][]);
    }
}