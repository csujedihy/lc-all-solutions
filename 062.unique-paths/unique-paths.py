class Solution(object):
  def uniquePaths(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    dp = [1] * n

    for i in range(1, m):
      pre = 1
      for j in range(1, n):
        dp[j] = dp[j] + pre
        pre = dp[j]
    return dp[-1]
