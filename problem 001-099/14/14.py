from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = str()
        if not strs:
            return common_prefix
        if len(strs) == 1:
            return strs[0]
        for char_index, char in enumerate(strs[0]):
            for string in strs[1:]:
                if len(string) <= char_index:
                    return common_prefix
                if string[char_index] != char:
                    return common_prefix
            common_prefix += char
        return common_prefix
        

if __name__ == "__main__":
    input_list = [
        [],
        ["hi"],
        ["hello", "hi"],
        ["hi", "hello"],
        ["flow", "flower", "fling"],
        ["flower", "flow", "flaw"],
        ["ab", "a"],
        ["flower", "flowing", "flow"]
    ]
    for input_item in input_list:
        output = Solution().longestCommonPrefix(input_item)
        print("Input=", input_item)
        print("Output=", output, "\n")