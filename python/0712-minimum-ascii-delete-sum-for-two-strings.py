class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        track = [[None for _ in range(m + 1)] for _ in range(n + 1)]

        def dp(i, j):
            if i == m or j == n:
                return ("", 0)

            if track[j][i] is not None:
                return track[j][i]

            if s1[i] == s2[j]:
                string, val = dp(i + 1, j + 1)
                res = (s1[i] + string, ord(s1[i]) + val)
            else:
                left = dp(i + 1, j)
                right = dp(i, j + 1)
                res = max(left, right, key=lambda x: x[1])

            track[j][i] = res
            return res

        total = sum(ord(c) for c in s1 + s2)
        result = total - 2 * dp(0, 0)[1]
        print("DP table (string, ascii_sum):")
        for row in track[:-1]:
            print(" | ".join(str(cell) for cell in row[:-1]))
        return result


Solution().minimumDeleteSum("ccaccjp", "fwosarcwge")
