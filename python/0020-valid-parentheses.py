from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                c2 = stack.pop()
                if not (
                    c2 == "("
                    and c == ")"
                    or c2 == "["
                    and c == "]"
                    or c2 == "{"
                    and c == "}"
                ):
                    return False
        return len(stack) == 0


print(Solution().isValid("(){}{}"))
