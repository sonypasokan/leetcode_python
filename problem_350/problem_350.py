from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        p1 = 0
        output_list = list()
        while len(nums2) > 0 and p1 < len(nums1):
            if nums1[p1] in nums2:
                output_list.append(nums1[p1])
                nums2.remove(nums1[p1])
            p1 += 1
        return output_list
        
if __name__ == "__main__":
    input_list = [
        [[1,2,2,1], [2,2]],
        [[4,9,5], [9,4,9,8,4]]
    ]
    for input_item in input_list:
        print("Input=", input_item)
        output = Solution().intersect(input_item[0], input_item[1])
        print("Output=", output, "\n")