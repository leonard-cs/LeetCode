from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        target = newInterval[0]
        left, right = 0, len(intervals) - 1

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        intervals.insert(left, newInterval)

        result = []
        for inter in intervals:
            if result and inter[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], inter[1])
            else:
                result.append(inter)
        return result
