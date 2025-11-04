class Solution251104:
    def smallestNumber(self, n: int) -> int:
        print(f"n = {n:b}")
        result = (1 << len(bin(n)[2:])) - 1
        print(f"result = {result:b}")
        print(result)
        return result
