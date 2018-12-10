class Solution(object):
  def longestLine(self, M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    if not M:
      return 0
    hor = [[0] * (len(M[0]) + 2) for _ in range(len(M) + 1)]
    ver = [[0] * (len(M[0]) + 2) for _ in range(len(M) + 1)]
    diag = [[0] * (len(M[0]) + 2) for _ in range(len(M) + 1)]
    anti = [[0] * (len(M[0]) + 2) for _ in range(len(M) + 1)]
    ans = 0
    for i in range(len(M)):
      for j in range(len(M[0])):
        if M[i][j] == 1:
          hor[i + 1][j + 1] = hor[i + 1][j] + 1
          ver[i + 1][j + 1] = ver[i][j + 1] + 1
          diag[i + 1][j + 1] = diag[i][j] + 1
          anti[i + 1][j + 1] = anti[i][j + 2] + 1
          ans = max(ans, hor[i + 1][j + 1], ver[i + 1][j + 1], diag[i + 1][j + 1], anti[i + 1][j + 1])
    return ans
