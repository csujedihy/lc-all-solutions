class Solution(object):
  def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    if len(word1) == 0 or len(word2) == 0:
      return max(len(word1), len(word2))

    dp = [[0] * (len(word2) + 1) for _ in range(0, len(word1) + 1)]
    dp[0][0] = 0

    for i in range(0, len(word1) + 1):
      for j in range(0, len(word2) + 1):
        if i == 0:
          dp[i][j] = j
        elif j == 0:
          dp[i][j] = i
        else:
          cond1 = dp[i][j - 1] + 1
          cond2 = dp[i - 1][j] + 1
          cond3 = 0
          if word1[i - 1] == word2[j - 1]:
            cond3 = dp[i - 1][j - 1]
          else:
            cond3 = dp[i - 1][j - 1] + 1
          dp[i][j] = min(cond1, cond2, cond3)
    return dp[-1][-1]
