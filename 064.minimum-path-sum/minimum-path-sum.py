class Solution(object):
  def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if len(grid) == 0:
      return 0
    dp = [0 for _ in range(0, len(grid[0]))]
    dp[0] = grid[0][0]

    for j in range(1, len(grid[0])):
      dp[j] = dp[j - 1] + grid[0][j]

    for i in range(1, len(grid)):
      pre = dp[0] + grid[i][0]
      for j in range(1, len(grid[0])):
        dp[j] = min(dp[j], pre) + grid[i][j]
        pre = dp[j]
      dp[0] += grid[i][0]

    return dp[-1]
