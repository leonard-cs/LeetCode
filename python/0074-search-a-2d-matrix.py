from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            y = (top + bottom) // 2
            if target > matrix[y][-1]:
                top = y + 1
            elif target < matrix[y][0]:
                bottom = y - 1
            else:
                break
        if not (top <= bottom):
            return False
        y = (top + bottom) // 2
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            x = (left + right) // 2
            if target > matrix[y][x]:
                left = x + 1
            elif target < matrix[y][x]:
                right = x - 1
            else:
                return True
        return False
