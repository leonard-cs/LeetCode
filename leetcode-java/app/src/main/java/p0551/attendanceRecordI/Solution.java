package p0551.attendanceRecordI;

public class Solution {
    public boolean checkRecord(String s) {
        char[] chars = s.toCharArray();
        int absentCount = 0;
        int consecutiveLate = 0;
        for (char ch : chars) {
            switch (ch) {
                case 'P':
                    consecutiveLate = 0;
                    break;
                case 'A':
                    consecutiveLate = 0;
                    absentCount++;
                    if (absentCount >= 2) return false;
                    break;
                case 'L':
                    consecutiveLate++;
                    if (consecutiveLate >= 3) return false;
                    break;
                default:
            }
        }
        return true;
    }
}
