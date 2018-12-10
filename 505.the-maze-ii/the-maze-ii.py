class Solution(object):
  def shortestDistance(self, maze, ball, hole):
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: int
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
        yield (i, j), dist

    heap = [(0, tuple(ball))]
    visited = set()
    hole = tuple(hole)
    while heap:
      dist, curr = heapq.heappop(heap)
      if curr in visited:
        continue
      visited |= {curr}
      if curr == hole:
        return dist
      for pos, incDist in next(curr, maze):
        heapq.heappush(heap, (dist + incDist, pos))

    return -1
