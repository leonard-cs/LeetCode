class Solution251002:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        length: int = min(len1, len2)
        merged = []

        for i in range(length):
            merged.append(word1[i])
            merged.append(word2[i])

        if len1 > len2:
            merged.append(word1[length:])
        elif len2 > len1:
            merged.append(word2[length:])
        return "".join(merged)
