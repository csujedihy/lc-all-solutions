class Solution(object):
  def checkRecord(self, n):
    """
    :type n: int
    :rtype: int
    """
    M = 10 ** 9 + 7
    dp = [0] * (n + 1)
    dp[:3] = [1, 2, 4]

    for i in range(3, n + 1):
      dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % M
    ans = dp[n]

    for i in range(1, n + 1):
      ans += (dp[i - 1] * dp[n - i]) % M
      ans %= M
    return ans % M
