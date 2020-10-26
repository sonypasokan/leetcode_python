class Solution:
    def isHappy(self, n: int) -> bool:
        sum_set = set([2, 3])
        num_sum = n
        n = str(n)

        while num_sum != 1:
            num_sum = 0
            for digit in n:
                num_sum += int(digit) * int(digit)
            print("sum=", num_sum)
            if num_sum in sum_set:
                return False
            sum_set.add(num_sum)
            n = str(num_sum)
        return True


if __name__ == "__main__":
    input_list = [
        19,
        20,
        1
    ]
    for input_item in input_list:
        print("input=", input_item)
        output = Solution().isHappy(input_item)
        print("output=", output)