from collections import deque


class Solution(object):
  def hasPath(self, maze, start, destination):
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: bool
    """

    def next(curr, maze):
      height = len(maze)
      width = len(maze[0])
      directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
      for di, dj in directions:
        dist = 0
        i, j = curr
        while 0 <= i + di < height and 0 <= j + dj < width and maze[i + di][j + dj] != 1:
          i += di
          j += dj
          dist += 1
        yield (i, j)

    queue = deque([tuple(start)])
    visited = set()
    destination = tuple(destination)
    while queue:
      curr = queue.popleft()
      if curr in visited:
        continue
      if curr == destination:
        return True
      visited |= {curr}
      for nbr in next(curr, maze):
        queue.append(nbr)
    return False
