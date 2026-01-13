
"""
Best Time to Buy and Sell Stock
===============================

Problem:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Idea:
Use a single pass (One Pass) approach.
Keep track of the minimum price found so far (`min_price`).
For every price, calculate the potential profit (`price - min_price`) and update `max_profit` if it's higher than the current max.

Complexity:
- Time: O(N)
- Space: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Finds the maximum profit possible using One Pass.
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if not prices: 
            return 0

        min_price = float('inf')
        max_profit = 0

        for p in prices:
            if p < min_price: 
                min_price = p
            elif p - min_price > max_profit:
                max_profit = p - min_price
        
        return max_profit

    def maxProfitNaive(self, prices: List[int]) -> int:
        """
        Naive approach using nested loops.
        Time Complexity: O(N^2)
        Space Complexity: O(N^2) in the original implementation (matrix), or O(1) if optimized.
        """
        max_gain = 0
        n = len(prices)
        # Original implementation used O(N^2) space for gain matrix, which is unnecessary.
        # gain = [[0] * n for _ in range(n)]

        for i in range(n): 
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                if profit > max_gain:
                    max_gain = profit
        return max_gain

if __name__ == "__main__":
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Prices: {prices}")
    print(f"Max Profit (One Pass): {solution.maxProfit(prices)}")
    print(f"Max Profit (Naive): {solution.maxProfitNaive(prices)}")