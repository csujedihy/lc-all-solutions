from collections import deque


class Solution(object):
  def shortestDistance(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    def bfs(si, sj, grid, buildNum, hit):
      dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
      queue = deque([(si, sj, 0)])
      visited = set([(si, sj)])
      count = 1
      while queue:
        i, j, dist = queue.popleft()
        for di, dj in dirs:
          newi, newj = i + di, j + dj
          if (newi, newj) in visited:
            continue
          if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]) and grid[newi][newj] != 2:
            if grid[newi][newj] != 1:
              grid[newi][newj] -= dist + 1
              hit[newi][newj] += 1
              visited |= {(newi, newj)}
              queue.append((newi, newj, dist + 1))
            else:
              count += 1
            visited |= {(newi, newj)}

      if count != buildNum:
        print
        count, buildNum
        return False
      return True

    count = 0
    for i in range(0, len(grid)):
      for j in range(0, len(grid[0])):
        if grid[i][j] == 1:
          count += 1

    hit = [[0] * len(grid[0]) for _ in range(0, len(grid))]
    for i in range(0, len(grid)):
      for j in range(0, len(grid[0])):
        if grid[i][j] == 1:
          if not bfs(i, j, grid, count, hit):
            return -1

    ans = float("-inf")
    for i in range(0, len(grid)):
      for j in range(0, len(grid[0])):
        if grid[i][j] < 0 and hit[i][j] == count:
          ans = max(ans, grid[i][j])
          grid[i][j] = 0
    return -ans if ans != float("-inf") else -1
