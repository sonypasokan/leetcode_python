class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for index, char in enumerate(haystack):
            if haystack[index:].startswith(needle):
                return index
        if haystack == needle:
            return 0
        return -1

if __name__ == "__main__":
    input_list = [
        ["hello","ll"],
        ["aaaaa", "bba"],
        ["", ""],
        [" ", ""],
        ["", "he"]
    ]
    for input_item in input_list:
        print("Input=", input_item)
        output = Solution().strStr(input_item[0], input_item[1])
        print("Output=", output, "\n")