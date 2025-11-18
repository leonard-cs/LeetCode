from pprint import pprint
from typing import List


class Solution251118:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        stack = [(sr, sc)]
        value = image[sr][sc]
        m, n = len(image), len(image[0])
        while stack:
            r, c = stack.pop()
            image[r][c] = color
            if r - 1 >= 0 and image[r - 1][c] == value:  # top
                stack.append((r - 1, c))
            if c - 1 >= 0 and image[r][c - 1] == value:  # left
                stack.append((r, c - 1))
            if r + 1 < m and image[r + 1][c] == value:  # bottom
                stack.append((r + 1, c))
            if c + 1 < n and image[r][c + 1] == value:  # right
                stack.append((r, c + 1))
        return image


pprint(Solution251118().floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
