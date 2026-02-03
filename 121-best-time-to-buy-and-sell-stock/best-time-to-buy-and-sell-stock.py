# Problem: Best Time to Buy and Sell Stock
# Pattern: Greedy / One Pass
# Time Complexity: O(n)
# Space Complexity: O(1)
# Key Idea: Track minimum price so far and maximum profit

class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit
