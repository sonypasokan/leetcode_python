from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buying_price = 0
        selling_price = 0
        
        for day_count, stock_price in enumerate(prices):
            if day_count == 0:
                # Stock cannot be sold without buying
                buying_price = stock_price
                continue
            
            if stock_price < buying_price:
                buying_price = stock_price
                selling_price = 0
            elif stock_price > selling_price:
                selling_price = stock_price
            else:
                continue
            current_profit = selling_price - buying_price
            max_profit = max(max_profit, current_profit)

        return max_profit

if __name__ == "__main__":
    input_list = [
        [7,1,5,3,6,4],
        [7,6,4,3,1],
        [7,6,1,10,2,20],
        [2,4,10,8,2,10,30]
    ]
    for input_item in input_list:
        print("input = ", input_item)
        output = Solution().maxProfit(input_item)
        print("output=", output)