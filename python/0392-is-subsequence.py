class Solution251003:
    def isSubsequence(self, s: str, t: str) -> bool:
        pos = 0
        for char in s:
            new_pos = t[pos:].find(char)
            if new_pos == -1:
                return False
            else:
                pos += new_pos + 1
        return True
