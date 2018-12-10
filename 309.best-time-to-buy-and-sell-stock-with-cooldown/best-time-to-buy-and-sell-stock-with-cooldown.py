class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
      return 0
    buy = [0] * len(prices)
    sell = [0] * len(prices)
    buy[0] = -prices[0]
    buy[1] = max(-prices[1], buy[0])
    sell[0] = 0
    sell[1] = max(prices[1] - prices[0], 0)
    for i in range(2, len(prices)):
      buy[i] = max(sell[i - 2] - prices[i], buy[i - 1])
      sell[i] = max(prices[i] + buy[i - 1], sell[i - 1])
    return max(sell)
