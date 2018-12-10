class Solution(object):
  def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
      return False

    m = len(matrix)
    n = len(matrix[0])

    start, end = 0, m * n - 1
    while start + 1 < end:
      mid = start + (end - start) / 2
      if matrix[mid / n][mid % n] > target:
        end = mid
      elif matrix[mid / n][mid % n] < target:
        start = mid
      else:
        return True
    if matrix[start / n][start % n] == target:
      return True
    if matrix[end / n][end % n] == target:
      return True
    return False
