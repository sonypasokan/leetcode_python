class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for char in s[::-1]:
            if char == " " and count > 0:
                break
            if char != " ":
                count += 1
        return count
        
if __name__ == "__main__":
    input_list = [
        "Hello World",
        "Hi Sony",
        "a ",
        " "
    ]
    for input_item in input_list:
        print("input=", input_item)
        output = Solution().lengthOfLastWord(input_item)
        print("output=", output)
