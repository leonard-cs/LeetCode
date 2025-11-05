from typing import List


class Solution251105:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = None
        count = 0
        for n in nums:
            if n != seen:
                seen = n
                nums[count] = seen
                count += 1
        return count
