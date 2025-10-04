class Solution251004:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        is_vowel = [1 if c in vowel else 0 for c in s]
        current_sum = sum(is_vowel[:k])
        if current_sum == k:
            return k
        result = current_sum
        for i in range(k, len(is_vowel)):
            current_sum = current_sum - is_vowel[i - k] + is_vowel[i]
            result = max(result, current_sum)
            if result == k:
                return k
        return result
