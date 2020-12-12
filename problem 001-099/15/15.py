from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        triplets = list()
        nums.sort()
        for index in range(len(nums)):
            if nums[index] > 0:
                break # After this no numbers can together make a sum of 0
            if index == 0 or nums[index] != nums[index-1]:
                self.__two_sum(nums, index, triplets)
        return triplets
    
    def __two_sum(self, number_list, index, triplets):
        first_ptr = index + 1
        last_ptr = len(number_list) - 1
        while (first_ptr < last_ptr):
            triplet_sum = number_list[index] + number_list[first_ptr] + number_list[last_ptr]
            if triplet_sum < 0:
                first_ptr += 1
            elif triplet_sum > 0:
                last_ptr -= 1
            else:
                triplets.append([number_list[index], number_list[first_ptr], number_list[last_ptr]])
                first_ptr += 1
                last_ptr -= 1
                while(first_ptr < last_ptr and number_list[first_ptr] == number_list[first_ptr-1]):
                    first_ptr += 1

if __name__ == "__main__":
    input_list = [
        [1],
        [1,2],
        [1,2,0],
        [-1,0,1,1],
        [-1,0,1,2,-1,-4],
        [0,0,0]
    ]
    for input_item in input_list:
        print("input=", input_item)
        output = Solution().threeSum(input_item)
        print("output=", output, "\n")