package p0697.arrayDegree;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int findShortestSubArray(int[] nums) {
        Map<Integer, int[]> map = new HashMap<>();
        int maxCount = 0;
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int[] meta;
            if (map.containsKey(num)) {
                meta = map.get(num);
                meta[0] = meta[0] + 1;
                maxCount = Math.max(maxCount, meta[0]);
                meta[2] = i;
            } else {
                meta = new int[]{1, i, i};
                maxCount = Math.max(maxCount, 1);
            }
            map.put(num, meta);
        }

        int shortest = Integer.MAX_VALUE;
        for (int[] meta : map.values()) {
            if (meta[0] == maxCount) {
                shortest = Math.min(shortest, meta[2] - meta[1] + 1);
            }
        }
        return shortest;
    }
}
