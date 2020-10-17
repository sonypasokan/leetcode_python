from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = dict()

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(word)
            else:
                anagram_map[sorted_word] = [word]
        
        return list(anagram_map.values())
        

if __name__ == "__main__":
    input_list = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ["a"]
    ]
    for input_item in input_list:
        output = Solution().groupAnagrams(input_item)
        print("Input=", input_item)
        print("Output=", output, "\n")