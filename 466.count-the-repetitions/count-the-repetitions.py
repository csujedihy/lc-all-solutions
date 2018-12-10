class Solution(object):
  def getMaxRepetitions(self, s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    l2 = len(s2)
    dp = [0] * l2
    for i in range(l2):
      j = i
      for c in s1:
        if c == s2[j % l2]:
          j += 1
      if j == i:
        return 0
      dp[i] = j - i

    idx = 0
    for i in range(n1):
      idx += dp[idx % l2]
    return idx / l2 / n2
