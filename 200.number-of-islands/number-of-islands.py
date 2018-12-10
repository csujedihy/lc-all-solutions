class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    visited = set()
    ans = 0

    def dfs(grid, i, j, visited):
      if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0" or (i, j) in visited:
        return False
      visited |= {(i, j)}
      for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        newi, newj = i + di, j + dj
        dfs(grid, newi, newj, visited)
      return True

    for i in range(0, len(grid)):
      for j in range(0, len(grid[0])):
        if dfs(grid, i, j, visited):
          ans += 1
    return ans
