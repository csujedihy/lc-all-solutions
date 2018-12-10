class Solution(object):
  def uniquePathsWithObstacles(self, grid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    if not grid:
      return 0
    if grid[0][0] == 1:
      return 0
    dp = [[0] * len(grid[0]) for _ in range(0, len(grid))]
    dp[0][0] = 1 if grid[0][0] == 0 else 0
    for i in range(1, len(grid)):
      if grid[i][0] == 0:
        dp[i][0] = 1
      else:
        break

    for j in range(1, len(grid[0])):
      if grid[0][j] == 0:
        dp[0][j] = 1
      else:
        break

    for i in range(1, len(grid)):
      for j in range(1, len(grid[0])):
        if grid[i][j] == 1:
          dp[i][j] = 0
        else:
          dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]
