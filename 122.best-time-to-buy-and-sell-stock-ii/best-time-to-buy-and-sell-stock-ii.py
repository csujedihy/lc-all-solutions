class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # [7, 1, 5, 3, 6, 4]
        if not prices:
            return 0
        ans = 0
        start = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                ans += prices[i-1] - start
                start = prices[i]
        ans += max(prices[-1] - start, 0)
        return ans