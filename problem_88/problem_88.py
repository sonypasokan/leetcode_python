from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        index = len(nums1) - 1
        while p2 >= 0:
            if p1 < 0 or nums2[p2] > nums1[p1]:
                large_val = nums2[p2]
                p2 -= 1
            else:
                large_val = nums1[p1]
                p1 -= 1
            nums1[index] = large_val
            index = index - 1

if __name__ == "__main__":
    input_list = [
        [[1,2,3,0,0,0],3, [2,5,6],3],
        [[2,0], 1, [1], 1]
    ]
    for input_item in input_list:
        Solution().merge(input_item[0], input_item[1], input_item[2], input_item[3])
        print("Input=", input_item)
        print("Output=", input_item[0], "\n")