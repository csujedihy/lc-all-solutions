class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = buy2 = float("-inf")
        sell1 = sell2 = 0
        for i in xrange(0, len(prices)):
            buy1 = max(-prices[i], buy1)
            sell1 = max(buy1 + prices[i], sell1)
            buy2 = max(sell1 - prices[i], buy2)
            sell2 = max(buy2 + prices[i], sell2)
        return sell2