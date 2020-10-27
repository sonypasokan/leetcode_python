from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_map = dict()
        for index, num in enumerate(numbers):
            if num in num_map:
                if num == target / 2:
                    return num_map[num] + 1, index + 1
                continue
            remainder = target - num
            if remainder in num_map:
                return num_map[remainder] + 1, index + 1
            num_map[num] = index
        return None, None

if __name__ == "__main__":
    input_list = [
        [[1,2,3,4,5], 5],
        [[1, 1, 2,3, 4,5], 3],
        [[2,7,11,15], 9]
    ]
    for input_item in input_list:
        print("input=", input_item)
        output = Solution().twoSum(input_item[0], input_item[1])
        print("output=", output)