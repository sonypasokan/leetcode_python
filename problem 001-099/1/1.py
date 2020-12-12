class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = dict()
        for index, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [num_map[diff], index]
            num_map[num] = index

if __name__ == "__main__":
    input_list = [
        [[1,2,3,4,5], 3],
        [[2,3,4], 6],
        [[10,20,30,3,40,3],6],
        [[30,40,50,0,9,29], 29],
        [[20,30,28],50],
        [[10,10], 20],
        [[1,1,3,4,5], 2],
        [[30,40,50,60], 100],
        [[101,202,202], 404],
        [[1,2,3,4,5,6,7,8,9,10,23,34,45,46,47,48], 33]
    ]
    for input_item in input_list:
        print("Input = ", input_item, end=" ")
        output = Solution().twoSum(input_item[0], input_item[1])
        print("Output = ", output)