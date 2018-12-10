from collections import deque


class Solution(object):
  def updateMatrix(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    queue = deque([])
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
          queue.append((i, j))
        if matrix[i][j] == 1:
          matrix[i][j] = -1

    while queue:
      i, j = queue.popleft()
      for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] == -1:
          matrix[ni][nj] = matrix[i][j] + 1
          queue.append((ni, nj))
    return matrix
