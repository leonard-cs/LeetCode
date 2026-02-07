package p3379.transformedarray;


class Solution {
    public static int[] constructTransformedArray(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            if (num > 0) {
                int index = (i + num) % n;
                result[i] = nums[index];
            } else if (num < 0) {
                int index = (i + num) % n;
                index = (index >= 0) ? index : n + index;
                result[i] = nums[index];
            } else {
                result[i] = nums[i];
            }
        }
        return result;
    }
}
