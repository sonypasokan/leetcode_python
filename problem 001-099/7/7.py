class Solution:
    def reverse(self, x: int) -> int:
        if self.is_signed_int_32_bit(x) == False:
            return 0
        output_int = 0
        if x < 0:
            negative_value = True
            x = abs(x)
        else:
            negative_value = False
        while (x != 0):
            remainder = x % 10
            output_int = output_int * 10 + remainder
            x = int(x / 10)
        if negative_value:
            output_int = -output_int
        if self.is_signed_int_32_bit(output_int) == False:
            return 0
        return int(output_int)
    
    def is_signed_int_32_bit(self, number):
        if abs(number) < 2**31 and number != 2**31 - 1:
            return True
        return False



if __name__ == "__main__":
    input_items = [
        123,
        -123,
        0,
        -9999,
        1563847412, # Will exceed the range
    ]
    for item in input_items:
        output = Solution().reverse(item)
        print("Input=", item)
        print("Output=", output, "\n")