class Solution(object):
  def maxKilledEnemies(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
      return 0
    dpRow = [[0] * (len(grid[0]) + 2) for _ in range(0, len(grid) + 2)]
    dpCol = [[0] * (len(grid[0]) + 2) for _ in range(0, len(grid) + 2)]

    for i in range(0, len(grid)):
      for j in range(0, len(grid[0])):
        dpRow[i + 1][j + 1] = dpRow[i + 1][j]
        dpCol[i + 1][j + 1] = dpCol[i][j + 1]
        if grid[i][j] == "W":
          dpRow[i + 1][j + 1] = 0
          dpCol[i + 1][j + 1] = 0
        if grid[i][j] == "E":
          dpRow[i + 1][j + 1] += 1
          dpCol[i + 1][j + 1] += 1

    maxKilled = 0
    for i in reversed(range(0, len(grid))):
      for j in reversed(range(0, len(grid[0]))):
        if grid[i][j] == "W":
          continue
        dpRow[i + 1][j + 1] = max(dpRow[i + 1][j + 1], dpRow[i + 1][j + 2])
        dpCol[i + 1][j + 1] = max(dpCol[i + 1][j + 1], dpCol[i + 2][j + 1])
        if grid[i][j] == "0":
          maxKilled = max(maxKilled, dpRow[i + 1][j + 1] + dpCol[i + 1][j + 1])
    return maxKilled
