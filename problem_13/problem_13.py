class Solution:
    def __init__(self):
        self.symbol_map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
    def romanToInt1(self, s: str) -> int:
        integer = 0
        for index, char in enumerate(s):
            if char in ("I", "X", "C") and index + 1 < len(s) and (
                (char == "I" and s[index + 1] in ("V", "X")) or \
                (char == "X" and s[index + 1] in ("L", "C")) or \
                (char == "C" and s[index + 1] in ("D", "M"))):
                integer = integer - self.symbol_map[char]
            else:
                value = self.symbol_map[char]
                integer += value
        return integer
    def romanToInt(self, s: str) -> int:
        integer = 0
        index = 0
        while index < len(s):
            char = s[index]
            if char in ("I", "X", "C") and index + 1 < len(s) and (
                (char == "I" and s[index + 1] in ("V", "X")) or \
                (char == "X" and s[index + 1] in ("L", "C")) or \
                (char == "C" and s[index + 1] in ("D", "M"))):
                integer = integer - self.symbol_map[char] + self.symbol_map[s[index + 1]]
                index += 2
            else:
                integer += self.symbol_map[char]
                index += 1
        return integer




if __name__ == "__main__":
    input_list = [
        "III",
        "IV",
        "IX",
        "LVIII",
        "MCMXCIV",
        "DCXXI", #621
    ]
    for input_item in input_list:
        print("input=", input_item)
        output = Solution().romanToInt(input_item)
        print("output=", output)