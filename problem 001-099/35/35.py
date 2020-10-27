from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target)
    
    def binary_search(self, number_list, search_item, index=0):
        length = len(number_list)
        if length == 1:
            if number_list[0] >= search_item:
                return index
            else:
                return index + 1
        mid_index = abs(int(length / 2))
        mid_element = number_list[mid_index]
        if mid_element == search_item:
            return index + mid_index
        elif mid_element < search_item:
            new_index = index + mid_index
            return self.binary_search(number_list[mid_index:], search_item, new_index)
        else:
            return self.binary_search(number_list[:mid_index], search_item, index)
        

if __name__ == "__main__":
    input_data = [
        [[1], 2],
        [[2], 2],
        [[3], 2],
        [[1,2,3], 2],
        [[1,2,3,4,5], 3],
        [[1,2,3,4,5,6], 6],
        [[1,2,3,4,5,6,7], 7],
        [[1,2,3,4,5,6,7], 1],
        [[1,2,3,4,5,6], 1],
        [[1,2,3,4,5,6,7],2],
        [[1,2,3,4,5,6], 2],
        [[1,2,3,5,6,7,8],4],
        [[1,2,3,4,5,6], 7],
        [[1,2,3,4,5,6,7], 8]
    ]
    for item in input_data:
        output = Solution().searchInsert(item[0], item[1])
        print("Input=", item)
        print("Output=", output, "\n")
        