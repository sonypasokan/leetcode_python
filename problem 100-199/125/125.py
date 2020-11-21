class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = [char.lower() for char in s if char.isalnum()]
        reverse_index = len(char_list) - 1
        for char in char_list:
            if reverse_index < len(char_list) / 2: return True
            if char != char_list[reverse_index]: return False
            reverse_index -= 1
        return True

if __name__ == "__main__":
    input_list = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "0P"
    ]
    for input_item in input_list:
        print("Input=", input_item)
        output = Solution().isPalindrome(input_item)
        print("Output=", output)