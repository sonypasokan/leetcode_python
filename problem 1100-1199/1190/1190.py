class Solution:
    def reverseParentheses(self, s: str) -> str:
        open_brace_indices = list()
        index = 0
        while index < len(s):
            print("i=", index)
            char = s[index]
            if char == "(":
                open_brace_indices.append(index)
                index += 1
            elif char == ")":
                last_open_index = open_brace_indices.pop()
                s = s[:last_open_index] + s[last_open_index + 1 : index][::-1] + s[index + 1:]
                index -= 1
            else:
                index += 1
        return s
                

        
if __name__ == "__main__":
    input_list = [
        "hi",
        "(hello)hi",
        "(hello)",
        "(u(love)i)",
        "(ed(et(oc))el)"
    ]
    for input_item in input_list:
        print("Input=", input_item)
        output = Solution().reverseParentheses(input_item)
        print("Output=", output, "\n")