import math


class Solution251002:  # ! WRONG
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""
        if str1[0] != str2[0]:
            return result

        if len(str1) > len(str2):
            prefix = str2
        else:
            prefix = str1

        for i in range(1, len(prefix) + 1):
            pre = prefix[:i]
            print(pre)
            x, y = 0, 0
            quit = False
            while x < len(str1) and not quit:
                if str1[x] != pre[x % len(pre)] and len(str1) % len(pre) == 0:
                    quit = True
                x += 1
            quit = False
            while y < len(str2) and not quit:
                if str2[y] != pre[y % len(pre)] and len(str2) % len(pre) == 0:
                    quit = True
                y += 1
            result = pre if not quit else ""
        return result


class Solution251005:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        gcd_len = math.gcd(len1, len2)
        gcd_string = str1[:gcd_len]
        if str1 == gcd_string * (len1 // gcd_len) and str2 == gcd_string * (
            len2 // gcd_len
        ):
            return gcd_string
        return ""


class SolutionLeetCode:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(len1, len2):
            while len2:
                len1, len2 = len2, len1 % len2
            return len1

        return str1[: gcd(len(str1), len(str2))]
