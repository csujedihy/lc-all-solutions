class NumMatrix(object):
  def __init__(self, matrix):
    """
    initialize your data structure here.
    :type matrix: List[List[int]]
    """
    self.dp = [[0] * len(matrix[0]) for i in range(0, len(matrix))]
    for i in range(0, len(matrix)):
      for j in range(0, len(matrix[0])):
        if i == 0:
          self.dp[0][j] = self.dp[0][j - 1] + matrix[i][j]
        elif j == 0:
          self.dp[i][0] = self.dp[i - 1][0] + matrix[i][j]
        else:
          self.dp[i][j] = self.dp[i - 1][j] + self.dp[i][j - 1] - self.dp[i - 1][j - 1] + matrix[i][j]

  def sumRegion(self, row1, col1, row2, col2):
    """
    sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
    :type row1: int
    :type col1: int
    :type row2: int
    :type col2: int
    :rtype: int
    """
    dp = self.dp

    diagSum = dp[row1 - 1][col1 - 1]
    totalSum = dp[row2][col2]
    leftSum = dp[row2][col1 - 1]
    upSum = dp[row1 - 1][col2]
    if row1 == 0:
      upSum = 0
      diagSum = 0
    if col1 == 0:
      leftSum = 0
      diagSum = 0
    return totalSum - leftSum - upSum + diagSum
