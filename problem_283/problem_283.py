from typing import List

class Solution:    
    def moveZeroes(self, nums: List[int]) -> None:
        slow_ptr = 0
        for fast_ptr, number in enumerate(nums):
            if number != 0:
                nums[slow_ptr], nums[fast_ptr] = nums[fast_ptr], nums[slow_ptr]
                slow_ptr += 1            

        
if __name__ == "__main__":
    input_list = [
        [1,2,3,4],
        [1,2,3,0,4],
        [1,2,3,0,0,4,1],
        [1,2,3,4,0,3,0,5,9]
    ]
    for input_item in input_list:
        print("\ninput=", input_item)
        Solution().moveZeroes(input_item)
        print("output=", input_item)