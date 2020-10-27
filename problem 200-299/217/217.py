from typing import List

class Solution:
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = dict()
        for num in nums:
            if num in num_dict:
                return True
            num_dict[num] = None
        return False

if __name__ == "__main__":
    input_list = [
        [1,2,3,4,1,2,3,4,5],
        [4,1,1,2,3,2,3],
        [1,2,3]
    ]
    for input_item in input_list:
        print("Input=", input_item)
        output = Solution().containsDuplicate(input_item)
        print("Output=", output, "\n")
        