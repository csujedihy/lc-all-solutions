class Solution(object):
  def generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    ans = [[1] * n for n in range(1, numRows + 1)]
    for i in range(1, numRows + 1):
      for j in range(0, i - 2):
        ans[i - 1][1 + j] = ans[i - 2][j] + ans[i - 2][j + 1]
    return ans
