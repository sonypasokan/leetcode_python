from typing import List

class Solution:
    def __init__(self):
        self.letter_map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
    def letterCombinations(self, digits: str) -> List[str]:
        words_list = list()

        for digit in digits:
            if not digit in digits:
                continue
            if not words_list:
                words_list = list(self.letter_map[digit])
                continue
            temp_words_list = list()
            for word in words_list:
                for char in self.letter_map[digit]:
                    temp_words_list.append(word + char)
            words_list = temp_words_list
        return words_list
        

if __name__ == "__main__":
    input_list = [
        "234",
        "23",
        "",
        "2"
    ]
    for input_item in input_list:
        print("input=", input_item)
        output = Solution().letterCombinations(input_item)
        print("output=", output)
