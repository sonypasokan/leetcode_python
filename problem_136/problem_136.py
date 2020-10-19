from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_map = dict()
        for number in nums:
            if number in num_map:
                num_map.pop(number)
            else:
                num_map[number] = None
        for number in num_map:
            return number

if __name__ == "__main__":
    input_list = [
        [1,2,3,4,1,2,3,4,5],
        [4,1,1,2,3,2,3]
    ]
    for input_item in input_list:
        print("Input=", input_item)
        output = Solution().singleNumber(input_item)
        print("Output=", output, "\n")