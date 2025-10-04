from typing import List


class Solution251004:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result: List[bool] = []
        for candie in candies:
            result.append(candie + extraCandies >= max_candies)
        return result
