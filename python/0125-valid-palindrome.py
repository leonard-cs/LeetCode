class Solution251107:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(c.lower() for c in s if c.isalpha() or c.isdigit())
        left, right = 0, len(new_s) - 1
        while left < right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1
        return True
