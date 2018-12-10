class Solution(object):
  def maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if len(matrix) == 0:
      return 0
    dp = [[0] * len(matrix[0]) for i in range(0, len(matrix))]
    ans = 0
    for i in range(0, len(matrix)):
      for j in range(0, len(matrix[0])):
        if matrix[i][j] == "1":
          if i == 0:
            dp[i][j] = 1
          elif j == 0:
            dp[i][j] = 1
          else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
          ans = max(ans, dp[i][j])
    return ans * ans
