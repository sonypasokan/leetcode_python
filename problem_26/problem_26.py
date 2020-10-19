from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        while count < len(nums):
            while count + 1 < len(nums) and nums[count + 1] == nums[count]:
                nums.pop(count)
            count += 1
        return count

if __name__ == "__main__":
    input_list = [
        [1,2,3,4,5],
        [1,2,2],
        [1,1,2,2,3],
        [1,1,2],
        [0,0,1,1,1,2,2,3,3,4]
    ]
    for input_item in input_list:
        print("input=", input_item)
        output = Solution().removeDuplicates(input_item)
        print("output=", output, input_item)