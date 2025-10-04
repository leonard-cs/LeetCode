from typing import List


class Solution251004:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        result = current_sum
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            result = max(result, current_sum)
        return result / k
