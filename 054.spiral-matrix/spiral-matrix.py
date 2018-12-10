class Solution(object):
  def spiralOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
      return []
    ans = []
    left, up, down, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
    while left <= right and up <= down:
      for i in range(left, right + 1):
        ans += matrix[up][i],
      up += 1
      for i in range(up, down + 1):
        ans += matrix[i][right],
      right -= 1
      for i in reversed(range(left, right + 1)):
        ans += matrix[down][i],
      down -= 1
      for i in reversed(range(up, down + 1)):
        ans += matrix[i][left],
      left += 1
    return ans[:(len(matrix) * len(matrix[0]))]
