List = [7, 1, 5, 3, 6, 4]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        
        for price in prices:
            if price<min_price:
                min_price =price
            elif price - min_price > max_profit:
                max_profit = price-min_price

        return max_profit 


    
        