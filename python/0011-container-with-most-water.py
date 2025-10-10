from typing import List


class Solution251009:
    def maxArea(self, height: List[int]) -> int:
        left, r = 0, len(height) - 1
        max_volume = 0
        while left < r:
            width = r - left
            h = min(height[left], height[r])
            max_volume = max(max_volume, width * h)
            if height[left] > height[r]:
                r -= 1
            else:
                left += 1
        return max_volume
