class Solution(object):
  def kInversePairs(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    MOD = 10 ** 9 + 7
    upper = n * (n - 1) / 2
    if k == 0 or k == upper:
      return 1
    if k > upper:
      return 0
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(1, n + 1):
      temp = [1] + [0] * k
      for j in range(k + 1):
        temp[j] = (temp[j - 1] + dp[j]) % MOD
        if j - i >= 0:
          temp[j] = (temp[j] - dp[j - i]) % MOD
      dp = temp
    return dp[k]
