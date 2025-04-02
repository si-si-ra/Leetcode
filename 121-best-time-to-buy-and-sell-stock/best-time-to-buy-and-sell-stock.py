class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update the minimum price found so far
            else:
                max_profit = max(max_profit, price - min_price)  # Calculate potential profit

        return max_profit
        