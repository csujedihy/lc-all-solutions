import bisect


class Solution(object):
  def maxSumSubmatrix(self, matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    ans = float("-inf")
    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(0, len(matrix)):
      for j in range(0, len(matrix[0])):
        dp[i][j] = dp[i][j - 1] + matrix[i][j]
    for start in range(0, len(matrix[0])):
      for end in range(start, len(matrix[0])):
        sums = [0]
        subsum = 0
        for i in range(0, len(matrix)):
          if start > 0:
            subsum += dp[i][end] - dp[i][start - 1]
          else:
            subsum += dp[i][end]
          idx = bisect.bisect_left(sums, subsum - k)
          if idx < len(sums):
            ans = max(ans, subsum - sums[idx])
          bisect.insort(sums, subsum)
    return ans
