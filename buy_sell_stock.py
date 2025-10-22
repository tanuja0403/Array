class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0 

        for current_price in prices:
            current_profit = current_price - min_price 
            max_profit = max (max_profit , current_profit)
            min_price = min (current_price , min_price)
        return max_profit 