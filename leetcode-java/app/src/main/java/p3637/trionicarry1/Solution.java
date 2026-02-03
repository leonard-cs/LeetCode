package p3637.trionicarry1;

class Solution {
    public static boolean isTrionic(int[] nums) {
        int count = 0;
        int count2 = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (count == 0 || count == 2) {
                if (nums[i] > nums[i+1]) {
                    System.out.println("count = " + count + "; i = " + i);
                    count++;
                    count2 = 01;
                } else {
                    count2++;
                }
            } else if (count == 1) {
                if (nums[i] < nums[i+1]) {
                    System.out.println("count = " + count + "; i = " + i);
                    count++;
                    count2 = 1;
                } else {
                    count2++;
                }
            } else {
                return false;
            }
        }
        return count == 2 && count2 > 0;
    }

    public static void main(String[] args) {
        int[] nums = {1,3,5,4,2,6};
//        int[] nums = {2,1,3};
        System.out.println(isTrionic(nums));
    }
}
