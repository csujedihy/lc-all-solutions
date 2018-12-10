class Solution(object):
  def totalNQueens(self, n):
    """
    :type n: int
    :rtype: int
    """

    def dfs(path, n):
      if len(path) == n:
        return 1
      res = 0
      for i in range(n):
        if i not in path and isValidQueen(path, i):
          path.append(i)
          res += dfs(path, n)
          path.pop()
      return res

    def isValidQueen(path, k):
      for i in range(len(path)):
        if abs(k - path[i]) == abs(len(path) - i):
          return False
      return True

    return dfs([], n)
