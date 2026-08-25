"""
Approach:
#sicne you can make unlimited traansactions but hold at most one stock at a time, every increasing step can be taken as profit

#so instead of finding the ranges we can add to the profit if the difference is positive

Time and space: O(n), O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
        