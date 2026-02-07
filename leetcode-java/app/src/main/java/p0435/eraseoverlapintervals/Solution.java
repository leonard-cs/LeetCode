package p0435.eraseoverlapintervals;

import java.util.Arrays;

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (inter1, inter2) -> Integer.compare(inter1[0], inter2[0]));

        int removeCount = 0;
        int prevEnd = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            int[] interval = intervals[i];
            if (interval[0] < prevEnd) {
                prevEnd = Math.min(prevEnd, interval[1]);
                removeCount++;
            } else {
                prevEnd = interval[1];
            }
        }
        return removeCount;
    }
}
