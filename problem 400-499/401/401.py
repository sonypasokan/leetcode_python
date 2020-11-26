from typing import List

class Solution:
    HOUR_LED_COUNT = 4
    TOTAL_LED_COUNT = 10

    def __init__(self):
        self.times = list()

    def readBinaryWatch(self, num: int) -> List[str]:
        self.__back_track(num, 0, 0, 0)
        return self.times

    def __back_track(self, num, led_pos, hour, minute):
        if hour > 11 or minute > 59:
            return
        if num == 0:
            self.times.append("".join([str(hour), ":", str(minute).zfill(2)]))
            return
        for i in range(led_pos, Solution.TOTAL_LED_COUNT):
            if i < Solution.HOUR_LED_COUNT:
                self.__back_track(num - 1, i + 1, hour + 2**i, minute)
            else:
                self.__back_track(num - 1, i + 1, hour, minute + 2**(i-Solution.HOUR_LED_COUNT))
        

if __name__ == "__main__":
    input_list = [
        1,
        2
    ]
    for input_item in input_list:
        print("input=", input_item)
        output = Solution().readBinaryWatch(input_item)
        print("output=", output, "\n", len(output))
        