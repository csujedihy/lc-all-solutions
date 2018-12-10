from collections import deque

INF = 2147483647


class Solution(object):
  def wallsAndGates(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: void Do not return anything, modify rooms in-place instead.
    """
    queue = deque([])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(0, len(rooms)):
      for j in range(0, len(rooms[0])):
        if rooms[i][j] == 0:
          queue.append((i, j))

    while queue:
      i, j = queue.popleft()
      for di, dj in directions:
        p, q = i + di, j + dj
        if 0 <= p < len(rooms) and 0 <= q < len(rooms[0]) and rooms[p][q] == INF:
          rooms[p][q] = rooms[i][j] + 1
          queue.append((p, q))
