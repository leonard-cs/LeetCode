package p0338.countBits;

import java.util.Arrays;

public class Solution {
    public static int[] countBits(int n) {
        int[] result = new int[n+1];
        int offset = 0;
        int nextOffset = 1;
        for (int i = 1; i < n+1; i++) {
            if (i == nextOffset) {
                offset = nextOffset;
                nextOffset *= 2;
            }
            System.out.println("i="+i+" offset="+offset);
            result[i] = result[i - offset] + 1;
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(countBits(5)));
    }
}
