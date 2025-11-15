from typing import List


class Solution251115_1:  #! Too naive O(q * m*m) where q = len(queries), m = size of query
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat: List[List[int]] = [[0 for _ in range(n)] for _ in range(n)]
        for query in queries:
            for i in range(query[0], query[2] + 1):
                for j in range(query[1], query[3] + 1):
                    mat[i][j] += 1
        return mat


class SolutionNeetCode:  #* O(q + n*n)
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        prefix: List[List[int]] = [[0] * (n + 1) for _ in range(n + 1)]
        for x1, y1, x2, y2 in queries:
            prefix[x1][y1] += 1
            prefix[x1][y2 + 1] -= 1
            prefix[x2 + 1][y1] -= 1
            prefix[x2 + 1][y2 + 1] += 1
        mat: List[List[int]] = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                top_left = 0 if i == 0 or j == 0 else mat[i - 1][j - 1]
                top = 0 if i == 0 else mat[i - 1][j]
                left = 0 if j == 0 else mat[i][j - 1]
                mat[i][j] = prefix[i][j] - top_left + top + left
        return mat


# sol = Solution().rangeAddQueries(3, [[1, 1, 2, 2], [0, 0, 1, 1]])
# for row in sol:
#     print(row)
