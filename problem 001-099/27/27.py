from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        while index < len(nums):
            if nums[index] == val:
                nums.pop(index)
                continue
            index += 1
        return index

if __name__ == "__main__":
    input_list = [
        [[1,2,3,4,1,1,1], 1]
    ]
    for input_item in input_list:
        output = Solution().removeElement(input_item[0], input_item[1])
        print("Input=", input_item)
        print("Output=", output, "\n")