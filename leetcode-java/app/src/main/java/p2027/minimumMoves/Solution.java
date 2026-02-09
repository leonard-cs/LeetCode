package p2027.minimumMoves;

public class Solution {
    public static int minimumMoves(String s) {
        int i = 0;
        int numMoves = 0;
        while (i < s.length()) {
            if (s.charAt(i) == 'X') {
                numMoves++;
                i += 3;
            } else {
                i++;
            }
        }
        return numMoves;
    }
}
