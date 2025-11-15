from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = defaultdict(int)
        s2_subcount = defaultdict(int)

        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_subcount[s2[i]] += 1

        matches = 0
        for k, v in s1_count.items():
            if s2_subcount[k] == v:
                matches += 1

        for i in range(len(s1), len(s2)):
            if matches == len(s1_count):
                return True

            char = s2[i - len(s1)]
            s2_subcount[char] -= 1
            if char in s1_count and s1_count[char] == s2_subcount[char]:
                matches += 1
            elif char in s1_count and s1_count[char] == s2_subcount[char] + 1:
                matches -= 1

            char = s2[i]
            s2_subcount[s2[i]] += 1
            if char in s1_count and s1_count[char] == s2_subcount[char]:
                matches += 1
            elif char in s1_count and s1_count[char] == s2_subcount[char] - 1:
                matches -= 1

        return matches == len(s1_count)


print(Solution().checkInclusion("abc", "lecaabee"))
