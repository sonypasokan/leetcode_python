from typing import List
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        window_size = 1
        output_sum = 0
        while window_size <= len(arr):
            print("window=", window_size)
            for index in range(len(arr)):
                print("index=", index)
                if index + window_size <= len(arr):
                    output_sum += sum(arr[index : index + window_size])
                    print("sum=", output_sum)
            window_size += 2
        return output_sum

        
if __name__ == "__main__":
    input_list = [
        [1],
        [1,2],
        [1,2,3],
        [1,2,3,4]
    ]
    for input_item in input_list:
        print("\ninput=", input_item)
        output = Solution().sumOddLengthSubarrays(input_item)
        print("output=", output)
