class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = buy2 = float("-inf")
        sell1 = sell2 = 0
        
        for i in range(len(prices)):
            sell1 = max(prices[i] + buy1, sell1)
            buy1 = max(buy1, -prices[i])
            sell2 = max(sell2, prices[i] + buy2)
            buy2 = max(sell1 - prices[i], buy2)
        return max(sell1, sell2)