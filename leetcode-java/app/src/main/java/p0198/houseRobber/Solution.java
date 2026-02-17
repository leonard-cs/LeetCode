package p0198.houseRobber;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public int rob(int[] nums) {
        int[] memo = new int[nums.length+2];
        int n = nums.length;
        for (int i = n-1; i >= 0; i--) {
            memo[i] = Math.max(nums[i] + memo[i+2], memo[i+1]);
        }
        return memo[0];
    }
}
