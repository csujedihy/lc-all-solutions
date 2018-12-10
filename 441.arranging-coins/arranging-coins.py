class Solution(object):
  def arrangeCoins(self, n):
    """
    :type n: int
    :rtype: int
    """
    return int((((1 + 8 * n) ** 0.5) - 1) / 2)
