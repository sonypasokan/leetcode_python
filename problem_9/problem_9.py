class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        number = x
        reverse_number = 0
        while number > 0:
            remainder = number % 10
            reverse_number = reverse_number * 10 + remainder
            number = number // 10
        return x == reverse_number
        
if __name__ == "__main__":
    input_list = [
        -121,
        -101,
        121
    ]
    for input_item in input_list:
        print("Input=", input_item)
        output = Solution().isPalindrome(input_item)
        print("Output=", output, "\n")