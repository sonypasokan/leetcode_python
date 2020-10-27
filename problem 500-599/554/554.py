from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        sum_map = dict()
        for row in wall:
            sum_bricks = 0
            for col_index, brick_value in enumerate(row):
                if col_index == len(row) - 1:
                    continue
                sum_bricks += brick_value
                if sum_bricks in sum_map:
                    sum_map[sum_bricks] += 1
                else:
                    sum_map[sum_bricks] = 1
        max_count = 0
        for sum_bricks in sum_map:
            if max_count < sum_map[sum_bricks]:
                max_count = sum_map[sum_bricks]
        return len(wall) - max_count

if __name__ == "__main__":
    input_list = [
        [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]],


    ]
    for input_item in input_list:
        print("input=", input_item)
        output = Solution().leastBricks(input_item)
        print("output=", output)