class Solution(object):
  def nthUglyNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0] * (n + 1)
    dp[1] = 1
    i2 = i3 = i5 = 1
    for i in range(2, n + 1):
      dp[i] = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
      if dp[i] == dp[i2] * 2:
        i2 += 1
      if dp[i] == dp[i3] * 3:
        i3 += 1
      if dp[i] == dp[i5] * 5:
        i5 += 1
    return dp[-1]
