from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)  # tuple -> [string]
        for string in strs:
            count = [0] * 26
            for c in string.lower():
                count[ord(c) - ord("a")] += 1
            dict[tuple(count)].append(string)
        return list(dict.values())
