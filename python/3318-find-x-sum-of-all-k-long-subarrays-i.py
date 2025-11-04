from typing import List


class Solution251104:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def xSum(sub_nums: List[int], x: int) -> int:
            dict = {}
            for n in sub_nums:
                if n in dict:
                    dict[n] += 1
                else:
                    dict[n] = 1
            print(f"dict = {dict}")
            sorted_dict = sorted(dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
            print(f"sorted_dict = {sorted_dict}")
            sum = 0
            for i in range(min(len(sorted_dict), x)):
                sum += sorted_dict[i][0] * sorted_dict[i][1]
            print(f"sum = {sum}")
            return sum

        result = []
        for i in range(len(nums) - k + 1):
            sub_nums = nums[i : i + k]
            print(f"sub_nums = {sub_nums}")
            result.append(xSum(sub_nums, x))
            print()
        print(f"result = {result}")
        return result
