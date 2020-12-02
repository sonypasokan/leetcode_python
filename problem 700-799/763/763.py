from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        index_map = {char : index for index, char in enumerate(S)}
        output_list = list()

        second_ptr = 0
        start_index = 0
        for first_ptr, char in enumerate(S):
            second_ptr = max(index_map[char], second_ptr)
            if first_ptr == second_ptr:
                output_list.append(second_ptr - start_index + 1)
                start_index = first_ptr + 1
        return output_list

        
if __name__ == "__main__":
    input_list = [
        "ababcbacadefegdehijhklij"
    ]
    for input_item in input_list:
        print("input=", input_item)
        output = Solution().partitionLabels(input_item)
        print("output=", output)
