from typing import List
class Solution:
    
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_time = 0
        max_key = "z"
        for index, duration in enumerate(releaseTimes):
            diff_time = duration - (0 if index == 0 else releaseTimes[index - 1])
            if diff_time > max_time:
                max_time = diff_time
                max_key = keysPressed[index]
            elif diff_time == max_time:
                max_key = max(max_key, keysPressed[index])
        return max_key



if __name__ == "__main__":
    input_list = [
        [[9,29,49,50], "cbcd"],
        [[12,23,36,46,62], "spuda"],
        [[23,34,43,59,62,80,83,92,97], "qgkzzihfc"],
        [[20,21,22,42], "abcc"]

    ]
    for input_item in input_list:
        print("input=", input_item)
        output = Solution().slowestKey(input_item[0], input_item[1])
        print("output=", output)