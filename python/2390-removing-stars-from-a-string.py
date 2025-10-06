class Solution251004:  # ! WRONG and not clean
    def removeStars(self, s: str) -> str:
        i = -1
        result = []
        star = 0
        while i >= -len(s):
            if s[i] == "*":
                star += 1
            else:
                i -= star
                result.append(s[i])
                star = 0
            i -= 1
        result.reverse()
        return "".join(result)


class Solution201006:
    def removeStars(self, s: str) -> str:
        result = []
        for c in s:
            if c == "*":
                result.pop()
            else:
                result.append(c)
        return "".join(result)
