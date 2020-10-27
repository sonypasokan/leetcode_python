from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        if length <= 10:
            return []
        sequence_map = dict()
        output_list = list()
        for index in range(length):
            if index + 10 > length:
                break
            sub_string = s[index : index + 10]
            if not sub_string in sequence_map:
                sequence_map[sub_string] = 1
            elif sequence_map[sub_string] == 1:
                output_list.append(sub_string)
                sequence_map[sub_string] += 1
        return output_list
        

if __name__ == "__main__":
    input_list = [
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
        "AAAAAAAAAAA"
    ]
    for input_item in input_list:
        output = Solution().findRepeatedDnaSequences(input_item)
        print("Input=", input_item)
        print("Output=", output, "\n")