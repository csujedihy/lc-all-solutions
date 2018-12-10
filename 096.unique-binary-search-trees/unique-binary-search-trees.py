class Solution(object):
  def _numTrees(self, n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
      for j in range(1, i + 1):
        dp[i] += dp[j - 1] * dp[i - j]
    return dp[-1]

  def numTrees(self, n):
    ans = 1
    for i in range(1, n + 1):
      ans = ans * (n + i) / i
    return ans / (n + 1)
