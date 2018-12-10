class Solution(object):
  # space O(n^2)
  def _numDistinct(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0] * (len(t) + 1) for _ in range(0, len(s) + 1)]

    for i in range(0, len(s) + 1):
      dp[i][0] = 1

    for i in range(1, len(s) + 1):
      for j in range(1, len(t) + 1):
        dp[i][j] += dp[i - 1][j]
        if t[j - 1] == s[i - 1]:
          dp[i][j] += dp[i - 1][j - 1]

    return dp[-1][-1]

  def numDistinct(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [0] * (len(t) + 1)
    for i in range(1, len(s) + 1):
      pre = 1
      for j in range(1, len(t) + 1):
        tmp = dp[j]
        if t[j - 1] == s[i - 1]:
          dp[j] += pre
        pre = tmp
    return dp[-1]
