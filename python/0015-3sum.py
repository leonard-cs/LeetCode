from typing import List


class Solution251109:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            num0 = nums[i]
            if num0 > 0:
                break
            if i > 0 and num0 == nums[i - 1]:
                continue
            target = -num0
            l, r = i + 1, len(nums) - 1
            while l < r:
                num1, num2 = nums[l], nums[r]
                if num1 + num2 == target:
                    result.append((num0, num1, num2))
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif num1 + num2 > target:
                    r -= 1
                else:
                    l += 1
        return result
