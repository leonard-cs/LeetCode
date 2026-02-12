package p3714.longestBalancedSubstringII;

import java.util.Arrays;

class Solution {
    public int longestBalanced(String s) {
        int n = s.length() + 1;
        int[] aPrefix = new int[n];
        int[] bPrefix = new int[n];
        int[] cPrefix = new int[n];
        for (int i = 0; i < s.length(); i++) {
            int aInc = 0;
            int bInc = 0;
            int cInc = 0;
            switch (s.charAt(i)) {
                case 'a': {
                    aInc = 1;
                }
                case 'b': {
                    bInc = 1;
                }
                case 'c': {
                    cInc = 1;
                }
                aPrefix[i+1] = aPrefix[i] + aInc;
                bPrefix[i+1] = bPrefix[i] + bInc;
                cPrefix[i+1] = cPrefix[i] + cInc;
            }
        }
        for (int k = s.length(); k > 0; k--) {
            for (int i = 0; i < s.length() - k + 1; i ++) {
                System.out.println("k = " + k + " i = " + i);
                int aCount = aPrefix[i+k] - aPrefix[i+1];
                int bCount = bPrefix[i+k] - bPrefix[i+1];
                int cCount = cPrefix[i+k] - cPrefix[i+1];
                if (k >= s.length() - 2) System.out.println("a = " + aCount + " b = " + bCount + " c = " + cCount);
                if (aCount == bCount && bCount == cCount) {
                    return k;
                }
            }
        }
        System.out.println(Arrays.toString(aPrefix));
        System.out.println(Arrays.toString(bPrefix));
        System.out.println(Arrays.toString(cPrefix));
        return 0;
    }
}
