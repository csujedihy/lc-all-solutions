class Solution(object):

  def countPrimes(self, n):
    """
    :type n: int
    :rtype: int
    """

    def helper(n, dp):
      for i in range(2, n):
        if dp[i] == 1:
          k = i * i
          if k >= n:
            return
          while k < n:
            dp[k] = 0
            k += i

    if n < 2:
      return 0
    ans = 0
    dp = [1] * n
    dp[0] = 0
    dp[1] = 0
    helper(n, dp)
    # for i in range(0, n):
    #     if dp[i] == 1:
    #         print i + 1

    return sum(dp)
