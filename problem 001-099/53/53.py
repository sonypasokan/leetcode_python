from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for index, number in enumerate(nums[1 : ]):
            nums[index + 1] = max(number, number + nums[index])
            max_sum = max(max_sum, nums[index + 1])
        return max_sum

        
if __name__ == "__main__":
    input_list = [
        [-2,1,-3,4,-1,2,1,-5,4],
        [1],
        [0],
        [-1],
        [-2147483647]
    ]
    for input_item in input_list:
        print("Input=", input_item)
        output = Solution().maxSubArray(input_item)
        print("Output=", output, "\n")