from typing import List
import math


class Solution251108:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        result = max_pile
        l, r = 1, max_pile
        while l <= r:
            k = (l + r) // 2
            time = sum([math.ceil(pile / k) for pile in piles])
            print(f"k: {k}, time: {time}")
            if time <= h:  # too fast, eat slower
                result = k
                r = k - 1
            else:
                l = k + 1
        return result
