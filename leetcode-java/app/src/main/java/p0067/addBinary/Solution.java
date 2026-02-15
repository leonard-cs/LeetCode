package p0067.addBinary;

public class Solution {
    public String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder();

        int an = a.length();
        int bn = b.length();
        int n = Math.max(an, bn);
        
        char carry = '0';
        for (int i = 0; i < n; i++) {
            char ai = (i < an) ? a.charAt(an-i-1) : '0';
            char bi = (i < bn) ? b.charAt(bn-i-1) : '0';
            if (ai == bi && ai == '1') {  // 11
                result.append(carry);
                carry = '1';
            } else if (ai == bi && ai == '0') {  // 00
                result.append(carry);
                carry = '0';
            } else {  // 10
                if (carry == '1') {  // 11
                    result.append('0');
                } else {  // 10
                    result.append('1');
                }
            }
        }
        if (carry == '1') result.append(carry);
        return result.reverse().toString();
    }
}
