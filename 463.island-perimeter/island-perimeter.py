class Solution(object):
  def islandPerimeter(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    def helper(grid, i, j):
      res = 0
      if grid[i][j] == 0:
        return 0
      if i == 0 or i - 1 >= 0 and grid[i - 1][j] == 0:
        res += 1
      if i == len(grid) - 1 or i + 1 < len(grid) and grid[i + 1][j] == 0:
        res += 1
      if j == 0 or j - 1 >= 0 and grid[i][j - 1] == 0:
        res += 1
      if j == len(grid[0]) - 1 or j + 1 < len(grid[0]) and grid[i][j + 1] == 0:
        res += 1
      return res

    ans = 0
    for i in range(0, len(grid)):
      for j in range(0, len(grid[0])):
        ans += helper(grid, i, j)
    return ans
