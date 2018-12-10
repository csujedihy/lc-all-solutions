class Solution(object):
  def minimumTotal(self, triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    dp = [0] * len(triangle)
    dp[0] = triangle[0][0]
    for i in range(1, len(triangle)):
      pre = dp[0]
      for j in range(len(triangle[i])):
        tmp = dp[j]
        if j == 0:
          dp[j] = pre
        elif j == len(triangle[i]) - 1:
          dp[j] = pre
        else:
          dp[j] = min(dp[j], pre)
        dp[j] += triangle[i][j]
        pre = tmp
    return min(dp)
