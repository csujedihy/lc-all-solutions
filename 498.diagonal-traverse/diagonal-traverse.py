class Solution(object):
  def findDiagonalOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix:
      return []
    ans = []
    directions = [(-1, 1), (1, -1)]
    d = 0
    i = j = 0
    for _ in range(len(matrix) * len(matrix[0])):
      ans.append(matrix[i][j])
      di, dj = directions[d]
      i, j = i + di, j + dj
      if i < 0 and 0 <= j < len(matrix[0]):
        i = 0
      elif i >= len(matrix):
        i = len(matrix) - 1
        j -= 2 * dj
      elif 0 <= i < len(matrix) and j < 0:
        j = 0
      elif 0 <= i < len(matrix) and j >= len(matrix[0]):
        j = len(matrix[0]) - 1
        i -= 2 * di
      elif i < 0 and j >= len(matrix[0]):
        i = 1
        j -= dj
      else:
        continue
      d = ~d
    return ans
