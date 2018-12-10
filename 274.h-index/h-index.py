class Solution(object):
  def hIndex(self, citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    n = len(citations)
    dp = [0] * (n + 1)
    for c in citations:
      if c > n:
        dp[n] += 1
      else:
        dp[c] += 1

    total = 0
    for i in reversed(range(1, len(dp))):
      total += dp[i]
      if total >= i:
        return i
    return 0
