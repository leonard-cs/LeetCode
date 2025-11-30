from collections import deque
from typing import List


class Solution251129:  # * BFS (139ms)
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        inf = int(1e9)

        queue = deque()  # (r, c)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = inf

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (
                    0 <= nr < len(mat)
                    and 0 <= nc < len(mat[0])
                    and mat[nr][nc] > mat[r][c] + 1
                ):
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))

        return mat


class Solution251130:  # * DP (55ms)
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        inf = int(1e9)
        rows, cols = len(mat), len(mat[0])
        # top-left
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else inf
                    left = mat[r][c - 1] if c > 0 else inf
                    mat[r][c] = min(top, left) + 1

        # buttom-right
        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if mat[r][c] > 0:
                    buttom = mat[r + 1][c] if r < rows - 1 else inf
                    right = mat[r][c + 1] if c < cols - 1 else inf
                    mat[r][c] = min(mat[r][c], buttom + 1, right + 1)

        return mat
