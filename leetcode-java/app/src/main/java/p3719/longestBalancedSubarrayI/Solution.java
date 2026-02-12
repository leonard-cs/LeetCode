package p3719.longestBalancedSubarrayI;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int longestBalanced(int[] nums) {
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            Set<Integer> evenSet = new HashSet<>();
            Set<Integer> oddSet = new HashSet<>();
            for (int j = i; j < nums.length; j++) {
                if ((nums[j] & 1) == 0) {
                    evenSet.add(nums[j]);
                } else {
                    oddSet.add(nums[j]);
                }

                if (!evenSet.isEmpty() && evenSet.size() == oddSet.size()) {
                    ans = Math.max(ans, j - i + 1);
                }
            }
        }
        return ans;
    }
}
