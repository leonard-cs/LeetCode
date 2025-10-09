class Solution251009:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"
        str_list = list(s)
        pairs = []
        for i, c in enumerate(str_list):
            if c.lower() in vowels:
                pairs.append((c, i))
        num_vowels = len(pairs)
        for i in range(num_vowels):
            (c1, i1) = pairs[i]
            (c2, i2) = pairs[num_vowels - 1 - i]
            str_list[i1] = c2
            str_list[i2] = c1
        return "".join(str_list)
