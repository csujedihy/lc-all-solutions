import heapq


class Solution(object):
  def findShortestWay(self, maze, ball, hole):
    """
    :type maze: List[List[int]]
    :type ball: List[int]
    :type hole: List[int]
    :rtype: str
    """

    def next(curr, maze):
      height = len(maze)
      width = len(maze[0])
      directions = [(-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")]
      for di, dj, mark in directions:
        dist = 0
        i, j = curr
        while 0 <= i + di < height and 0 <= j + dj < width and maze[i + di][j + dj] != 1:
          i += di
          j += dj
          dist += 1
          if (i, j) == hole:
            break
        yield (i, j), mark, dist

    heap = [(0, "", tuple(ball))]
    visited = set()
    hole = tuple(hole)
    while heap:
      dist, word, curr = heapq.heappop(heap)
      if curr in visited:
        continue
      visited |= {curr}
      if curr == hole:
        return word
      for pos, mark, incDist in next(curr, maze):
        heapq.heappush(heap, (dist + incDist, word + mark, pos))

    return "impossible"
