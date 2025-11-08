from typing import List


class Solution251108:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            index = (l + r) // 2
            num = nums[index]
            if target == num:
                return index
            elif target > num:
                l = index + 1
            else:
                r = index - 1
        return -1
