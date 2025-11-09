class Solution251109:  # Runtime: 39ms
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
            count += 1
        return count


class Solution251109Math:  # Runtime: 0ms
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 > num2:
                count += num1 // num2
                num1 = num1 % num2
            else:
                count += num2 // num1
                num2 = num2 % num1
        return count
