package p1653.minimumdeletions;

public class Solution {
    public int minimumDeletions(String s) {
        int aCount = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'a') {
                aCount++;
            }
        }
        int bCount = 0;
        int minDeletions = s.length();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == 'a') {
                aCount--;
            }
            minDeletions = Math.min(minDeletions, aCount + bCount);
            if (ch == 'b') {
                bCount++;
            }
        }
        return minDeletions;
    }
}
