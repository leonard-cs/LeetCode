from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i in reversed(range(len(temperatures))):
            curr_temp = temperatures[i]
            if stack:
                while stack and curr_temp >= temperatures[stack[-1]]:
                    stack.pop()
                # curr_temp <= stack[-1]
                ans[i] = stack[-1] - i if stack else 0
            stack.append(i)

        return ans
