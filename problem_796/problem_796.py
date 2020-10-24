class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return True
        for index in range(len(A)):
            if A[index : ] + A[:index] == B:
                return True
        return False

if __name__ == "__main__":
    input_list = [
        ["sony", "onys"],
        ["hello", "he"],
        ["hello", "hello"],
        ["hello", "ohell"],
        ["abcde", "abced"],
        ["", ""]
    ]
    for input_item in input_list:
        print("input=", input_item)
        output = Solution().rotateString(input_item[0], input_item[1])
        print("output=", output)