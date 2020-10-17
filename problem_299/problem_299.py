class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        number_map = dict()
        a_count = 0
        b_count = 0
        a_indices = dict()
        for index, number in enumerate(secret):
            if guess[index] == number:
                a_count += 1
                a_indices[index] = None
            else:
                if number in number_map:
                    number_map[number].append(index)
                else:
                    number_map[number] = [index]
        
        for index, number in enumerate(guess):
            if index not in a_indices and number in number_map and number_map[number]:
                b_count += 1
                number_map[number].pop()
        
        return str(a_count) + "A" + str(b_count) + "B"

        
if __name__ == "__main__":
    input_list = [
        ["1807", "7810"],
        ["1123", "0111"],
        ["1", "0"],
        ["1", "1"],
        ["11", "10"]
    ]
    for input_item in input_list:
        output = Solution().getHint(input_item[0], input_item[1])
        print("Input=", input_item)
        print("Output=", output, "\n")