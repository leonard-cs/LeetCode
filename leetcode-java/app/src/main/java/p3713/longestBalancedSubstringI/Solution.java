package p3713.longestBalancedSubstringI;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int longestBalanced(String s) {
        int maxLength = 0;
        for (int i = 0; i < s.length() - maxLength; i++) {
            Map<Character, Integer> map = new HashMap<>();
            for (int j = i; j < s.length(); j++) {
                char ch = s.charAt(j);
                if (map.containsKey(ch)) {
                    map.put(ch, map.get(ch) + 1);
                } else {
                    map.put(ch, 1);
                }
                List<Integer> values = new ArrayList<>(map.values());
                int count = values.get(0);
                boolean flag = true;
                for (int value : values) {
                    if (value != count) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    maxLength = Math.max(maxLength, j-i+1);
                }
            }
        }
        return maxLength;
    }
}
