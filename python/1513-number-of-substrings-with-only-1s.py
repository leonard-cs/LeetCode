class Solution251116:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        result = count = 0
        for i in range(len(s)):
            if s[i] == "1":
                count += 1
            else:
                result = (result + (count * (count + 1)) // 2) % MOD
                count = 0
        result = (result + (count * (count + 1)) // 2) % MOD

        return result
