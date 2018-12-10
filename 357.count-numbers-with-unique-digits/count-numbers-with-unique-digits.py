class Solution(object):
  def countNumbersWithUniqueDigits(self, n):
    """
    :type n: int
    :rtype: int4
    """
    if n <= 1:
      return 10 ** n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 9
    k = 9
    for i in range(2, n + 1):
      dp[i] = max(dp[i - 1] * k, 0)
      k -= 1
    return sum(dp) + 1
