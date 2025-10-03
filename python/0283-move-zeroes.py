from typing import List


class Solution251003:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        number_of_nonzeros = 0
        for i in range(length):
            if nums[i] != 0:
                nums[number_of_nonzeros] = nums[i]
                number_of_nonzeros += 1
        for j in range(number_of_nonzeros, length):
            nums[j] = 0
