class Solution(object):
  def numberOfArithmeticSlices(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    ans = 0
    dp = [collections.defaultdict(int) for _ in A]
    for i in range(len(A)):
      for j in range(i):
        diff = A[i] - A[j]
        dp[i][diff] += 1
        if diff in dp[j]:
          dp[i][diff] += dp[j][diff]
          ans += dp[j][diff]
    return ans
